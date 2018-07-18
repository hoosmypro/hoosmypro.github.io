# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu

# a web crawler
import re
import requests

# configs
url_main = 'https://rabi.phys.virginia.edu/mySIS/CC2/'
web_regexp_config2 = """href=.(.*\.html)"""
web_regexp_config = """<a href=['"](.*)amp;(.*)amp;(.*)["']"""
url_prefix = ['https://rabi.phys.virginia.edu/mySIS/CC2/']
regexp_class = """\('([A-Z]{2,4})','(\d{2,4})'\);">(.+)<\/td><\/tr>"""
regexp_pro = """([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Za-z ]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)"""
regexp_des = """<td class="CourseNum">(.*)<\/td><td class="CourseName">.*\n.*class="CourseDescription">(.*?)<"""
page_to_search = [0,20]

dict_c = dict()
dict_p = dict()
dict_d = dict()

#\('([A-Z]{2,4})','(\d{2,4})'\);">(.+)<\/td><\/tr>
#([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Za-z ]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)
#([a-zA-Z]{2,}[- ]?[0-9]{4}).*<strong>([A-Z][a-z]+ [A-Z][a-z]+).*Name=([A-Z][a-z]+ [A-Z][a-z]+)
#\('([A-Z]{2,4})','(\d{2,4})'\);">([a-zA-Z \-,]+)<

def set_header(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115         Safari/537.36'}
    response = requests.get(url, headers=headers).text
    return response

def print_text(name_input):
    if name_input == "N":
        return
    file = open("output_"+name_input+ "_cla"+".txt","a")
    for key, values in dict_c.items():
        file.write(key+ " "+values[0]+'\n')
    file = open("output_" + name_input + "_pro" + ".txt", "a")
    for key, values in dict_p.items():
        a = ";".join(str(x) for x in values)
        file.write(key + " " + a + '\n')

def print_text1(name_input):
    if name_input == "N":
        return
    file = open("output_"+name_input+ "_cla"+".txt","a")
    for key, values in dict_d.items():
        file.write(key + " " + values + '\n')

def lookingforaddress(url_to_look_for):
    data1 = set_header(url_to_look_for)
    addresspattern = re.compile(web_regexp_config2)
    matches_s = re.findall(addresspattern, str(data1))
    matches_s = list_eliminate_duplicate(matches_s)
    return matches_s

def list_eliminate_duplicate(input_list):
    news_ids = []
    for id in input_list:
        if id not in news_ids:
            news_ids.append(id)
    return  news_ids

def lookingforpattern(string):

    zhPattern = re.compile(regexp_class)
    matches_c = re.findall(zhPattern, str(string))
    prPattern  = re.compile(regexp_pro)
    matches_p = re.findall(prPattern,str(string))

    print("Class matches found:"+str(len(matches_c)))
    print("Professor matches found:" + str(len(matches_p)))

    for items in matches_c:
        dict_c[items[0] + items[1]] = [items[2], []]

    for items in matches_p:
        if items[0] in dict_p:
            if(items[2] not in dict_p[items[0]]):
                dict_p[items[0]].append(items[2])
        else:
            dict_p[items[0]] = [items[2]]

def lookingforpattern2(string):

    zhPattern = re.compile(regexp_des)
    matches_c = re.findall(zhPattern, str(string))
    print(matches_c)

    print("Description matches found:"+str(len(matches_c)))
    for items in matches_c:
        dict_d["".join(items[0].split(" "))] = items[1]


def main_single(url_initial):
    lists = lookingforaddress(url_initial)
    print(lists)
    name_input = input("Enter the name of the output file. Enter 'N' to skip  ")
    for item in lists:
        for page in url_prefix:
            try:
                address = page + item
                # print(item[2].strip("Group=")+ " " + address)
                data = set_header(address)
                print("Start processing url:" + address )
                print("Status___Completed:" + str(lists.index(item) + 1) + "/" + str(len(lists)))
                data = str(data).replace("&nbsp;", "")##optional
                lookingforpattern2(data)
                break
            except:
                if url_prefix.index(page) == len(url_prefix) - 1:
                    print("Attempt Failed:Invalid URL")
    print_text1(name_input)

main_single(url_main)