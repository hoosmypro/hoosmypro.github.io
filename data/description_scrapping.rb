require 'open-uri'
require 'nokogiri'
require 'csv'
require "net/http"
require "watir"

# NOTE: install Selenium first (follow watir tutorial)

csv_options = { col_sep: ',', quote_char: '"', headers: :first_row }

BROWSER = Watir::Browser.new :chrome
#
details_array = []

# ==========================================================================
#                      USEFUL METHODS
# ==========================================================================

  # THIS METHOD CHECKS IF URL IS VALID
  def url_exist?(url_string)
    puts "Attempting #{url_string}"
    url = URI.parse(url_string)
    req = Net::HTTP.new(url.host, url.port)
    # UNCOMMENT LINE BELOW FOR HTTPS websites.
      # req.use_ssl = (url.scheme == 'https')
    path = url.path if url.path.present?
    res = req.request_head(path || '/')
    if res.kind_of?(Net::HTTPRedirection)
      return true # Go after any redirect and make sure you can access the redirected URL
    else
      ! %W(4 5).include?(res.code[0]) # Not from 4xx or 5xx families
    end
  rescue Errno::ENOENT
    false #false if can't find the server
  rescue URI::InvalidURIError
    false #false if URI is invalid
  rescue SocketError
    false #false if Failed to open TCP connection
  rescue Errno::ECONNREFUSED
    false #false if Failed to open TCP connection
  rescue Net::OpenTimeout
    false #false if execution expired
  rescue OpenSSL::SSL::SSLError
    false
  end

  # THIS METHOD IS FOR AUTO LOGIN IF NEEDED.

  def login
    link = "https://thecourseforum.com/"
    url = URI.parse(link)
    req = Net::HTTP.new(url.host, url.port)
    res = req.request_head(url.path)

    BROWSER.goto link
    sleep(2)
    page_prep_test = Nokogiri::HTML.parse(BROWSER.html)
    # TEST LOGIN
      BROWSER.input(id:"user_email").wait_until_present.send_keys("xz4ee@virginia.edu")
      BROWSER.input(id:"user_password").wait_until_present.send_keys("zaq123456")
      BROWSER.input(name: 'commit').wait_until_present.click

  end

  # THIS METHOD IS TO PARSE THE APP_MATERIALS TABLE

  def scrape_app_materials(i)
    link = "https://thecourseforum.com/departments/#{i}"
    url = URI.parse(link)
    req = Net::HTTP.new(url.host, url.port)
    res = req.request_head(url.path)

    BROWSER.goto link
    sleep(2)
    page_prep_test = Nokogiri::HTML.parse(BROWSER.html)
    # TEST LOGIN
    # login_if_needed(page_prep_test)

    page = Nokogiri::HTML.parse(BROWSER.html)
    # if page.search('div.error-num').text.strip == "500"
    #   return "NEXT"
    # else
    course_name = []
    course_description = []
    course_hash = {}
    page.search('div#browsing-content.container-fluid div#departments div.course-panel.current').each do |course|
      course_name << course.search('.course-name').inner_text
      course_description << course.search('.description').inner_text
    end
    # courses_materials_data_set.search('div.row.course-name').each_with_index do |n, i|
    #   course_name[i] = n.inner_text
    # end
    # courses_materials_data_set.search('.description').each_with_index do |d, index|
    #   des = d.text
    #   course_description[index] = des
    #   course_description[index] = "No description" if des.nil?
    # end
    course_hash = Hash[course_name.zip(course_description)]

    return course_hash
  end



# ==========================================================================
#                      SCRAPING START!
# ==========================================================================
  login
  (1..79).each do |i|
    # ---------------------------------------------------
    # SCRAPE PAGE W/ ID = i
    details_array << scrape_app_materials(i) #unless scrape_app_materials(i) == "NEXT"
    # ---------------------------------------------------

    # ---------------------------------------------------
    # SAVE ALL PAGES SCRAPED SO FAR...
    CSV.open("course_description.csv", "wb") do |csv|
      details_array.each do |hash|
        hash.each { |key, value| csv << [key, value] }
      end
    end
    # ---------------------------------------------------

    # ---------------------------------------------------
    # WAIT TO SATISFY ROBOTS.TXT
    sleep(4)
    # ---------------------------------------------------
  end

# TAKE HOME MESSAGES:

# STEP 1)  Check robots.txt for "crawl_delay"
# STEP 2)  Check if URL is VALID (before doing anything w/ Watir)
# STEP 3*) //IF LOGIN IS NEEDED, you can write a simple LOGIN method//
# STEP 4)  Design the button-clicking algorithm
# STEP 5)  NOKOGIRI PARSE! Get info, save into hash.
# STEP 6)  ON EACH ITERATION, SAVE INFO!! (csv or json!)

















