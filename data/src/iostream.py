# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu

import re

def readClassFile(file,dict): # file = name of file to read; dict = {class number:[names of professors]}
    file = open(file, 'r')
    for line in file:
        dict[line.split(" ", 1)[0]] = line.split(" ", 1)[1]

def readProFile(file,dict): # file = name of file to read; dict = {class number:[names of professors]}
    file2 = open(file, 'r')
    for line in file2:
        if line.split(" ", 1)[0] not in dict:
            dict[line.split(" ", 1)[0]] = line.split(" ", 1)[1].strip("\n").split(";")
        else:
            for item in line.split(" ", 1)[1].strip("\n").split(";"):
                if item not in dict[line.split(" ", 1)[0]]:
                    dict[line.split(" ", 1)[0]].append(item)

def readFiles(list,dic,dic_pro):
    for item in list:
        readClassFile(item + "_cla.txt",dic)
        readProFile(item + "_pro.txt", dic_pro)
    print(len(dic_pro)," professors loaded, ",len(dic)," classes loaded")

def generateFile(file_name,masterlist_of_Object):
    file1 = open(file_name+"_Category.txt",'w')
    file2 = open(file_name+"_Class.txt",'w')
    file3 = open(file_name+"_Instr.txt",'w')
    file4 = open(file_name+"_Section.txt",'w')
    for obj in masterlist_of_Object.values():
        print(obj.output())
        if obj.id //100000 ==1:
            file1.write(obj.output()+"\n")
        elif obj.id //100000 ==2:
            file2.write(obj.output()+"\n")
        elif obj.id //100000 ==3:
            file3.write(obj.output()+"\n")
        elif obj.id //100000 ==4:
            file4.write(obj.output()+"\n")
    file1.close()
    file2.close()
    file3.close()
    file4.close()

def getProName(str,dic):  # str: list of string, index 0 is class number, index 1 is comment, dic: dictionary[class index:list of professors]
    number = str[0].upper().replace(" ", "").replace("-", "")
    if(number not in dic):
        print(number + "Class number not found")
    else:
        for names in dic[number]:
            for name in names.split(" "):
                if name.upper() in str[1].upper():
                    return names
        if len(dic[number]) == 1:
            print("Warning 1")
            return dic[number][0]

    print(str)
    number = input(
        "Please manually enter a name or 'staff'; enter 'skip' to skip and ignore this class; enter 'store' to store this class and deal with it later")

    if (number == "skip"):
        return None
    return number

def getProName2017(str,dic):  # str: list of string, index 0 is class number, index 1 is comment, dic: dictionary[class index:list of professors]
    number = str[0].upper().replace(" ", "").replace("-", "")
    if(number not in dic):
        print(number + "Class number not found")
    else:
        for names in dic[number]:
            for name in names.split(" "):
                if name.upper() in str[2].upper():
                    return names
        if len(dic[number]) == 1:
            print("Warning: no matched instructor found, but returned the only one")
            return dic[number][0]
    print(str)
    number = input(
        "Please manually enter a name or 'staff'; enter 'skip' to skip and ignore this class; enter 'store' to store this class and deal with it later")

    if (number == "skip"):
        return None
    return number

def getClassName(number,dic):
    number = number.upper().replace(" ", "").replace("-", "")
    if(number in dic):
        return dic[number]
    else:
        print(number, "Class not found")
        while (True):
            number = input("Please manually enter a correct class name; enter 'skip' to skip and ignroe this class; enter 'store' to store this class and deal with it later")
            if(number == "skip"):
                return None
            if (number == "store"):
                return "store"
            if(number in dic):
                return dic[number]
            print(number, "class still not found")

def reg(regex,file_to_open): # list of findings is returned
    file = open(file_to_open,'r')
    addresspattern = re.compile(regex, flags= re.S)
    data = file.read()
    matches_s = re.findall(addresspattern, str(data))
    print(len(matches_s),'comments loaded')
    return matches_s