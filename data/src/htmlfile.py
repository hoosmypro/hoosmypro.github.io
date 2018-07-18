# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu

import cores
import iostream
import htmlscript

categoryInfo = dict()
classDescription = dict()

iostream.readCourseDescription("output_course_description_cla.txt",classDescription)
iostream.readCourseAbbr("cate_dis.txt",categoryInfo)




def generateHTML(output,dict):
    index = open(output+"index.html","w")
    index.write(htmlscript.temp_begin0)
    dictval = list(dict.values())
    dictval.sort(key=lambda x: x.name, reverse=True)
    print(dictval)
    for obj in dictval:
        file = open(output+str(obj.id)+".html",'w')

        if obj.id //100000 ==1:
            htmlscript.generateHTMLCategory(file,index,obj,dict,categoryInfo,classDescription)
        elif obj.id //100000 ==2:
            htmlscript.generateHTMLClass(file,index,obj,dict,categoryInfo,classDescription)
        elif obj.id //100000 ==3:
            htmlscript.generateHTMLInstr(file, index, obj, dict, categoryInfo, classDescription)

        #     file.write("<h1>Professor:" + obj.name + '</h1>' + "\n")
        #     file.write(
        #         "<h3>This professor is teaches or has taught following classes(click link to navigate)</h3>" + "\n")
        #     for item in obj.list_of_Class:
        #         file.write("<h5>"+dict[item].number+":"+dict[item].name+'</h5>')
        #         file.write('<a  href="'+str(item)+'.html"' +">"+dict[item].number+"</a>"+"\n")
        # elif obj.id //100000 ==4:
        #     continue # TODO implement file reader

    #     file.write(temp_end)
    index.write(htmlscript.temp_end0)

cores.repopulatingData("output/output")
cores.debug()
generateHTML("sample/",cores.masterlist_of_Object)
