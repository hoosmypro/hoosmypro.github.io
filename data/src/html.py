# Neal Haonan Chen
# University of Virginia
# hc4pa@virginia.edu

import cores

temp_begin = """<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>"""

temp_end = """</body>
</html>"""

def generateHTML(output,dict):
    index = open(output+"index.html","w")
    index.write(temp_begin)
    index.write("<h3>This is an index page that has links to all departments (click link to navigate)</h3>" + "\n")
    for obj in dict.values():
        file = open(output+str(obj.id)+".html",'w')
        file.write(temp_begin)
        if obj.id //100000 ==1:
            index.write('<a  href="' + str(obj.id) + '.html"' + ">" + obj.name + "</a>" + "\n")
            file.write("<h1>Department:"+obj.name+'</h1>'+"\n")
            file.write("<h3>This department has following classes(click link to navigate)</h3>" + "\n")
            for item in obj.list_of_Class:
                file.write("<h5>"+dict[item].number+":"+dict[item].name+'</h5>')
                file.write('<a  href="'+str(item)+'.html"' +">"+dict[item].number+"</a>"+"\n")
            file.write("<h3>This department has following professors(click link to navigate)</h3>" + "\n")
            for item in obj.list_of_Instructor:
                file.write("<h5>" + dict[item].name + '</h5>')
                file.write('<a  href="'+str(item)+'.html"' +">"+dict[item].name+"</a>"+"\n")
        elif obj.id //100000 ==2:
            file.write("<h1>Class:" + obj.number + ":" + obj.name + '</h1>' + "\n")
            file.write("<h3>Following professors have taught or are teaching this class(click link to navigate)</h3>" + "\n")
            for item in obj.list_of_Instructor:
                file.write("<h5>" + dict[item].name + '</h5>')
                file.write('<a  href="'+str(item)+'.html"' +">"+dict[item].name+"</a>"+"\n")
        elif obj.id //100000 ==3:
            file.write("<h1>Professor:" + obj.name + '</h1>' + "\n")
            file.write(
                "<h3>This professor is teaches or has taught following classes(click link to navigate)</h3>" + "\n")
            for item in obj.list_of_Class:
                file.write("<h5>"+dict[item].number+":"+dict[item].name+'</h5>')
                file.write('<a  href="'+str(item)+'.html"' +">"+dict[item].number+"</a>"+"\n")
        elif obj.id //100000 ==4:
            continue # TODO implement file reader

        file.write(temp_end)
    index.write(temp_end)

generateHTML("sample/",cores.repopulatingData("output/output"))
