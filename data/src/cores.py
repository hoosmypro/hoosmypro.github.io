# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu

import iostream

# ID is a six-digits code unique to a class/instructor/section/department. It is also used as an identifier when we create HTML pages
# Categories begin with 1; Classes begin with 2; instructors begin with 3; Sections begin with 4.

# Variables
counter = 0      #it tracks ID generation
# Masterlists that are used to get IDs by names/class numbers
masterlist_of_Category = dict() #{name:ID}
masterlist_of_Instructor = dict() #{name:ID}
masterlist_of_Class = dict() #{number:ID}
masterlist_of_Section = []
# Masterlist that is used to store and retrive objects by IDs {ID:object}
masterlist_of_Object = dict()

populatingData = dict()
dic = dict()              #dic stores raw data of classes
dic_pro = dict()          #dic stores raw data of professors
regexp_2018 = "([a-zA-Z]{2,}[- ]?[0-9]{4}):?(.*?)[\n,]{1,2}"
regexp_2017 = "([a-zA-Z-]{2,10}\s?\d{2,4})(.*?),(.*?),(.*?)[,\n](?=[,a-zA-Z-]{2,10}\s?[\d,]{3,4})"

#Configs
list1 = ["2015fall",'2016fall','2016sp','2017fall','2017sp','2018fall','2018sp']




class Category:

    def __init__(self,name):
        global counter
        counter += 1
        self.id = 100000 + counter           #Unique six digits ID, begins with 1 e.g. 100000
        self.name = name                     #Name of that category e.g. ENWR
        self.list_of_Class = []              #List of IDs of classes
        self.list_of_Instructor = []         #List of IDs of instructors
        masterlist_of_Category[name] = self.id
        masterlist_of_Object[self.id] = self

    def newAddition(self,number,name,pro,comments):
        classID = self.addClass(number,name)
        InstrID = self.addInstructor(pro)
        if classID not in masterlist_of_Object[InstrID].list_of_Class:
            masterlist_of_Object[InstrID].list_of_Class.append(classID)
        if InstrID not in masterlist_of_Object[classID].list_of_Instructor:
            masterlist_of_Object[classID].list_of_Instructor.append(InstrID)
        masterlist_of_Object[classID].addSection(InstrID,comments)

    def addInstructor(self,pro):
        if(pro not in masterlist_of_Instructor):
            temp = Instructor(pro)
            self.list_of_Instructor.append(temp.id)
        else:
            temp = masterlist_of_Object[masterlist_of_Instructor[pro]]
        return temp.id

    def addClass(self,number,name):
        if(number not in masterlist_of_Class):
            temp = Class(number,name,self.id)
            self.list_of_Class.append(temp.id)
        else:
            temp = masterlist_of_Object[masterlist_of_Class[number]]
        return temp.id

    def output(self):
        return str(self.id) +";"+ self.name +";" +str(self.list_of_Class) +";"+ str(self.list_of_Instructor)

    def populateData(self,id,list_class,list_instr):
        self.id = id
        for item in list_class:
            self.list_of_Class.append(int(item))
        for item in list_instr:
            try:
                self.list_of_Instructor.append(int(item))
            except:
                print(id,"Empty list")
        populatingData[self.id] = self


class Class:

    def __init__(self,number,name,belonged):
        global counter
        counter += 1
        self.id = 200000 + counter           #Unique six digits ID, begins with 2 e.g. 200000
        self.number = number                 #Number of this class e.g. CS2150
        self.name = name.strip("\n")         #Name of this class e.g. Intro to Programming
        self.list_of_Instructor = []         #List of IDs of instructors
        self.list_of_Section = []            #ID of sections it has
        self.belonged = belonged             #ID of the category it belongs to
        masterlist_of_Object[self.id] = self
        masterlist_of_Class[number] = self.id

    def addSection(self,InstrID,comments):
        temp = Section(self.number,self.name,InstrID,comments,self.id)
        self.list_of_Section.append(temp.id)

    def output(self):
        return  str(self.id) +";"+ self.number +";"+ self.name +";"+ str(self.list_of_Instructor) +";"+ str(self.list_of_Section)

    def populateData(self, id, list_instr,list_section):
        self.id = id
        for item in list_instr:
            self.list_of_Instructor.append(int(item))
        for item in list_section:
            self.list_of_Section.append(int(item))
        populatingData[self.id] = self


class Instructor:

    def __init__(self, name):
        global counter
        counter += 1
        self.id = 300000 + counter #Unique six digits ID, begins with 3 e.g. 300000
        self.name = name        #Instructor's name
        self.list_of_Class = [] #List of classes he/she teaches or taught
        masterlist_of_Object[self.id] = self
        masterlist_of_Instructor[name] = self.id

    def output(self):
        return  str(self.id) +";"+ self.name +";"+ str(self.list_of_Class)

    def populateData(self,id,list_class):
        self.id = id
        for item in list_class:
            self.list_of_Class.append(int(item))
        populatingData[self.id] = self


class Section:

    def __init__(self, number,name, instructor, comments, belong, difficult=0, hotness=0):
        global counter
        counter += 1
        self.id = 400000 + counter                    #Unique six digits ID, begins with 4 e.g. 400000
        self.number = number            #Class number e.g. CS2150
        self.name = name.strip("\n")                #Class name   e.g. Intro to Programming
        self.year = 2016                #To be used in future
        self.instructor = instructor    #ID of the instructor who teaches this class
        self.comment = comments
        self.difficult = difficult      #To be used in future
        self.hotness = hotness          #To be used in future
        self.belonged = belong          #The ID of class it belongs to
        masterlist_of_Object[self.id] = self
        masterlist_of_Section.append(self.id)

    def output(self):
        return str(self.id) +";"+ self.number +";"+ self.name +";"+ self.comment  +";"+ str(self.instructor) + ";"+str(self.belonged)

    def populateData(self,id):
        self.id = id
        populatingData[self.id] = self


# functions

def search_match(in_what,match):
    for item in in_what:
        if item == match:
            return item

def getObject(id):
    try:
        temp = masterlist_of_Object[id]
    except:
        print("Object not found!")
        return None
    return temp

def track():
    print(masterlist_of_Object)
    print(masterlist_of_Class)
    print(masterlist_of_Category)
    print(masterlist_of_Instructor)
    print(masterlist_of_Section)
    while(True):
        temp = input("Search object with ID; enter 'break' to quit")
        if temp == 'break':
            break
        print(getObject(int(temp)).output())

def initializeClass(number,name,pro,comments):
    abb = ''.join(filter(str.isalpha, number))
    abb = abb.upper()
    if abb not in masterlist_of_Category:
        temp = Category(abb)
    else:
        temp = masterlist_of_Object[masterlist_of_Category[abb]]
    temp.newAddition(number,name,pro,comments)

def repopulatingData(filename):
    list_cate, list_class, list_instr, list_section = iostream.readGeneratedFile(filename)
    for item in list_cate:
        a = Category(item[1])
        a.populateData(item[0],item[2],item[3])
    for item in list_class:
        a = Class(item[1],item[2],000000)
        a.populateData(item[0],item[3],item[4])
    for item in list_instr:
        a = Instructor(item[1])
        a.populateData(item[0],item[2])
    # for item in list_section:
    #     continue
    print(populatingData)
    return populatingData





def initialize(data, f2017 = False):
    print("Start manually handling unrecognized inputs")
    c = 0
    total = len(data)
    for line in data:
        name_Class = iostream.getClassName(line[0], dic)
        if name_Class == None:
            print(line, "is ignored")
            continue
        name_Class.strip('\n')
        if(f2017):
            name_Instr = iostream.getProName2017(line, dic_pro)
        else:
            name_Instr = iostream.getProName(line, dic_pro)
        if name_Instr == None:
            print(line, "is ignored")
            continue
        number = line[0].upper().replace(" ", "").replace("-", "")
        if(f2017):
            initializeClass(number, name_Class, name_Instr, line[3])
        else:
            initializeClass(number, name_Class, name_Instr, line[1])
        c += 1
        print("Progress", c, "/", total)
        # command = input("Command?")
        # if command == 'track':
        #     track()
        # if command == 'break':
        #     break
# iostream.readFiles(list1,dic,dic_pro)
# data_2018 = iostream.reg(regexp_2018,"Source_2018.csv")
# data_2017 = iostream.reg(regexp_2017,"Source_2017.csv")
# initialize(data_2017,True)
# initialize(data_2018)
# iostream.generateFile("output",masterlist_of_Object)



