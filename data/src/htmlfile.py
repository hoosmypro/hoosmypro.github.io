# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu

import cores
import iostream
import htmlscript

categoryInfo = dict()
classDescription = dict()
categoryWeb = dict()
courseURL = dict()

iostream.generalReader("data_course_description.txt", classDescription)
iostream.readCourseAbbr("cate_dis.txt",categoryInfo)
iostream.generalReader("data_LousWebsite.txt", categoryWeb)
iostream.generalReader("data_course_url.csv", courseURL, split= ",")

def generateHTML(output,dict):
    htmlscript.generateProfessorsPages(output)
    index = open(output+"index.html","w")
    index.write(htmlscript.temp_begin0)
    dictval = list(dict.values())
    dictval.sort(key=lambda x: x.name, reverse=False)
    print(dictval)
    for obj in dictval:
        file = open(output+str(obj.id)+".html",'w')

        if obj.id //100000 ==1:
            htmlscript.generateHTMLCategory(file,index,obj,dict,categoryInfo,classDescription)
        elif obj.id //100000 ==2:
            htmlscript.generateHTMLClass(file,index,obj,dict,categoryInfo,classDescription)
        elif obj.id //100000 ==3:
            htmlscript.generateHTMLInstr(file, index, obj, dict, categoryInfo, classDescription,output)
        elif obj.id //100000 ==4:
            htmlscript.generateHTMLSection(file, index, obj, dict, categoryInfo, classDescription,courseURL,categoryWeb)

    index.write(htmlscript.temp_end0)
    htmlscript.professorsPageWrapUp(output)
    print("Succeeded")

cores.repopulatingData("output/output")
cores.debug()
generateHTML("sample/",cores.masterlist_of_Object)
