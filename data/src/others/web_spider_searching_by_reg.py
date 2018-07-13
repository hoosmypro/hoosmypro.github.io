# Neal Chen
# hc4pa
# encoding:UTF-8
import urllib.request,urllib.parse,http.cookiejar
import re
import requests

#([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Z][a-z]+ [A-Z][a-z]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)
#[\u4e00-\u9fa5ABI0-9]*?[:∶：]?[  ]*?[\u4e00-\u9fa5， ()（）《》“”：？！。,.!?]*[\u4e00-\u9fa5][。？！?!！]

# Config
# To search with more than one key words
key_words = ["chinese-learning","chinese-sentence","chinese-speaking"]
# Basics
url_main = 'https://rabi.phys.virginia.edu/mySIS/CS2/'
web_regexp_config = """<a href=['"](.*)amp;(.*)amp;(.*)["']"""
url_prefix = ['https://rabi.phys.virginia.edu/mySIS/CS2/']
chinese_regexp = "([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Z][a-z]+ [A-Z][a-z]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)"
page_to_search = [0,20]
##########################
# Main


def main_single(url_initial):
    lists = lookingforaddress(url_initial)
    print(lists)
    name_input = input("Webspider is ready!Please type the name of the output file.")
    searchingaddress(lists, name_input)

def main_multi(url_inital,page_to_search):
    print("Task begins: Collecting URL from page "+str(page_to_search[0]),"to page "+str(page_to_search[1]))
    lists = []
    for page_no in range(page_to_search[0],page_to_search[1]):
        try:
            lists += lookingforaddress(url_inital + str(page_no + 1))
            lists = list_eliminate_duplicate(lists)
            print("Collecting URL......" + "__Number of URLs Found:" + str(len(lists)) + "__Completed Search:" + str(
                page_no + 1) + "/" + str(page_to_search[1]))
        except:
            print("404 Not Found, Searching aborted")
            break
    name_input = input("###Webspider is ready!Please type the name of the output file.###")
    lists = list_eliminate_duplicate(lists)
    searchingaddress(lists,name_input)

def main_multi_advance(url_inital,page_to_search):
    lists = []
    print("Task begins: looking for indexed page with " + str(len(key_words)) + " key words:")
    for key in range(0, len(key_words)):
        print("Looking for indexed page with key word:"+ key_words[key])
        url = url_inital + key_words[key] + "/page/"
        for page_no in range(page_to_search[0], page_to_search[1]):
            try:
                lists += lookingforaddress(url + str(page_no + 1))
                lists = list_eliminate_duplicate(lists)
                print(
                    "Collecting URL......" + "__Number of URLs Found:" + str(len(lists)) + "__Completed Search:" + str(
                        page_no + 1) + "/" + str(page_to_search[1]))
            except:
                print("404 Not Found: Searching aborted")
                break

    name_input = input("###Webspider is ready!Please type the name of the output file.###")
    lists = list_eliminate_duplicate(lists)
    searchingaddress(lists,name_input)


############################3
# Functional methods

def firewall_crackdown_and_decoding(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115         Safari/537.36'}

    response = requests.get(url, headers=headers).text
    return response

def searchingaddress(lists,name_input):
    for item in lists:
        for page in url_prefix:
            try:
                address = page + item[0] + item[1] + item[2]
                data = firewall_crackdown_and_decoding(address)
                print("Start processing url:" + address )
                print("Status___Completed:" + str(lists.index(item) + 1) + "/" + str(len(lists)))
                data = str(data).replace("&nbsp;", "")##optional
                lookingforchinese(data, name_input)
                break
            except:
                if url_prefix.index(page) == len(url_prefix) - 1:
                    print("Attempt Failed:Invalid URL")

def print_text(input_list,name_input):
    file = open("output_"+name_input+".txt","a")
    for items in input_list:
        for item in items:
            file.write(item+'\n')

def lookingforaddress(url_to_look_for):
    data1 = firewall_crackdown_and_decoding(url_to_look_for)
    addresspattern = re.compile(web_regexp_config)
    matches_s = re.findall(addresspattern, str(data1))
    matches_s = list_eliminate_duplicate(matches_s)
    return matches_s

def list_eliminate_duplicate(input_list):
    news_ids = []
    for id in input_list:
        if id not in news_ids:
            news_ids.append(id)
    return  news_ids

def lookingforchinese(string, name_input):
    zhPattern = re.zhPattern = re.compile(chinese_regexp)
    matches_s = re.findall(zhPattern, str(string))
    print("Match Found:"+str(len(matches_s)))
    print_text(matches_s, name_input)

main_single(url_main)
#Config:
#website: href="(\d*-\d*.*?.html)


# Config2:
# url_main = 'http://www.chineselearner.com/speaking/lesson/everyday-chinese2.html'
# web_regexp_config = 'href="\.{0,2}(.*\.html)'
# url_prefix = ["http://www.chineselearner.com/speaking/","http://www.chineselearner.com/speaking/lesson/"]

# config3
# url_main = 'http://www.hellomandarin.com/blog/category/business-chinese/page/'
# web_regexp_config = 'href="(http:\/\/www\.hellomandarin\.com\/blog\/\d{4}\/\d{2}\/\d{2}\/business-chinese-.*?)"'
# url_prefix = [""]
# chinese_regexp = "[\u4e00-\u9fa5ABI0-9]*?[:∶：][  ]*?[\u4e00-\u9fa5，()（）《》“”：？！。,.!?]*[\u4e00-\u9fa5][。？?!！]"
#web_regex: 'href="[\.\/]*(.*?\.htm)'