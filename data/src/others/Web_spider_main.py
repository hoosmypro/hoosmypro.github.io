# Neal Chen
# hc4pa  
from  web_spider_searching_by_reg import main_single, main_multi, main_multi_advance

#([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Z][a-z]+ [A-Z][a-z]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)

#config
key_words = ["chinese-learning","chinese-sentence","chinese-speaking"]
# Basics
url_main = 'https://rabi.phys.virginia.edu/mySIS/CS2/'
web_regexp_config = """ <a href=['"](.*)['"] """
url_prefix = ['']
chinese_regexp = "([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Z][a-z]+ [A-Z][a-z]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)"
page_to_search = [0,20]

def main():
    print("Web Spider Initiated!")
    print("Targeted main URL:" + url_main)
    print("Method a : single search: collecting URL from a single targeted page, and find all matches from collected URLs individually")
    print(
        "Method b : multiply search: collecting URL from several targeted pages, and find all matches from collected URLs individually")
    print(
        "Method c : advanced multiply search: searching targeted page with key words first, then collecting URL from several targeted pages, and find all matches from collected URLs individually")

    method = input("Which method would you like to use?")
    if method == "a":
        main_single(url_main)
    elif method == "b":
        main_multi(url_main,page_to_search)
    elif method == "c":
        main_multi_advance(url_main,page_to_search)
    else:
        print("Invalid input; enter a, b or c.")

main()