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

  def url_exist?(url_string)
    puts "Attempting #{url_string}"
    url = URI.parse(url_string)
    req = Net::HTTP.new(url.host, url.port)

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


  def login
    link = "https://thecourseforum.com/"
    url = URI.parse(link)
    req = Net::HTTP.new(url.host, url.port)
    res = req.request_head(url.path)

    BROWSER.goto link
    sleep(2)
    page_prep_test = Nokogiri::HTML.parse(BROWSER.html)
    BROWSER.input(id:"user_email").wait_until_present.send_keys("xz4ee@virginia.edu")
    BROWSER.input(id:"user_password").wait_until_present.send_keys("zaq123456")
    BROWSER.input(name: 'commit').wait_until_present.click

  end


  def scrape_app_materials(i)
    link = "https://thecourseforum.com/departments/#{i}"
    url = URI.parse(link)
    req = Net::HTTP.new(url.host, url.port)
    res = req.request_head(url.path)

    BROWSER.goto link
    sleep(2)
    page_prep_test = Nokogiri::HTML.parse(BROWSER.html)

    page = Nokogiri::HTML.parse(BROWSER.html)

    course_name = []
    course_description = []
    course_hash = {}
    page.search('div#browsing-content.container-fluid div#departments div.course-panel.current').each do |course|
      course_name << course.search('.course-name').inner_text
      course_description << course.search('.description').inner_text
    end
    course_hash = Hash[course_name.zip(course_description)]

    return course_hash
  end

  login
  (1..79).each do |i|
    details_array << scrape_app_materials(i)

    CSV.open("course_description.csv", "wb") do |csv|
      details_array.each do |hash|
        hash.each { |key, value| csv << [key, value] }
      end
    end
    sleep(4)
  end












