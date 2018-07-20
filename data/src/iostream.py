# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu

# stores functions specifically for reading and storing files
import re


def generalReader(file, dict,split = " "):
    file = open(file, "r")
    for line in file:
        temp = line.split(split,1)
        if(len(temp) <2):
            print(temp)
            dict[temp[0]] = ""
        else:
            dict[temp[0]] = temp[1]
    print(file , " has been loaded")

def readCourseAbbr(file,dict):
    file = open(file,"r")
    bool = True
    temp = ''
    for line in file:
        line = line.strip().strip("\n")
        if bool:
            bool = False
            temp = line
        else:
            bool = True
            dict[line] = temp

def readClassFile(file,dict): # file = name of file to read; dict = {class number:[names of classes]}
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
        if obj.id // 100000 == 1:
            file1.write(obj.output()+"\n")
        if obj.id // 100000 == 2:
            file2.write(obj.output()+"\n")
        if obj.id // 100000 == 3:
            file3.write(obj.output()+"\n")
        if obj.id // 100000 == 4:
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

# Read generated files

def readGeneratedFile(file_name):
    file1 = open(file_name+"_Category.txt",'r')
    list_cate = []
    for line in file1:
        temp = line.strip('\n').split(";")
        if(len(temp)!=4):
            print(len(temp))
            print("Error")
        temp2 = [int(temp[0]),temp[1],temp[2].lstrip("[").rstrip("]").split(", "),temp[3].lstrip("[").rstrip("]").split(", ")]
        list_cate.append(temp2)

    file2 = open(file_name+"_Class.txt",'r')
    list_class = []
    for line in file2:
        temp = line.strip('\n').split(";")
        if(len(temp)!=5):
            print(line)
            print("Error")
        temp2 = [int(temp[0]),temp[1],temp[2],temp[3].lstrip("[").rstrip("]").split(", "),temp[4].lstrip("[").rstrip("]").split(", ")]
        list_class.append(temp2)

    file3 = open(file_name+"_Instr.txt",'r')
    list_instr = []
    for line in file3:
        temp = line.strip('\n').split(";")
        if(len(temp)!=3):
            print("Error")
        temp2 = [int(temp[0]),temp[1],temp[2].lstrip("[").rstrip("]").split(", ")]
        list_instr.append(temp2)

    file4 = open(file_name+"_Section.txt",'r')
    list_section = []
    reg_pattern = "(\d{6});([A-Z]*\d*);(.*);(.*);(\d{6});(\d{6})"
    addresspattern = re.compile(reg_pattern)
    for line in file4:
        temp = re.findall(addresspattern, line.strip('\n').strip('"'))[0]
        if(len(temp)!=6):
            print(temp)
            print(len(temp))
            print("Error")
        temp2 = [int(temp[0]),temp[1],temp[2],temp[3],int(temp[4]),int(temp[5])]
        list_section.append(temp2)
    return list_cate,list_class,list_instr,list_section