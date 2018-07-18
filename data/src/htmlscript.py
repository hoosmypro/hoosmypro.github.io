# Neal Chen
# hc4pa  

#This file is used to store bulky python scripts

version = "v2.1.3"
temp_begin0 = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Departments</title>
    <!-- Bootstrap -->
    <link href="css/bootstrap-4.0.0.css" rel="stylesheet">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light col-lg-12"><a class="navbar-brand" href="https://www.msnatuva.org/"><img src="LOGO.png" width="50" height="30" alt="msn logo"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active"> <a class="nav-link" href="index.html">Hoos My Professor<span class="sr-only"></span></a> </li>
          <li class="nav-item"> <a class="nav-link" href="departmetnts.html">Departments<span class="sr-only">(current)</span></a></li>
			<li class="nav-item"> <a class="nav-link" href="professors.html">Professors</a></li>
          <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> 其他 </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#"></a> <a class="dropdown-item" href="#"></a><!drop down里的内容>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#"></a> <!drop down里的内容>
            </div>
          </li>
          <li class="nav-item"> </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
  </nav>

    <hr>
    <h2 class="text-center">Departments</h2>
    <hr>

    <hr>
        <div class="container">
      <div id="accordion">
  <div>
    <table>"""
temp_end0 = """</table>
  </div>
    </div>
			</div>
    <hr>

    <footer class="text-center">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <p>HoosMyProfessor © 2018 """ + version+ """All rights reserved.</p>
          </div>
        </div>
      </div>
    </footer>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="js/jquery-3.2.1.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap-4.0.0.js"></script>
  </body>
</html>"""
temp_begin1 = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>CS</title>
    <!-- Bootstrap -->
    <link href="css/bootstrap-4.0.0.css" rel="stylesheet">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light col-lg-12"><a class="navbar-brand" href="https://www.msnatuva.org/"><img src="LOGO.png" width="50" height="30" alt="msn logo"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active"> <a class="nav-link" href="index.html">Hoos My Professor</a> </li>
          <li class="nav-item"> <a class="nav-link" href="departmetnts.html">Departments</a></li>
			<li class="nav-item"> <a class="nav-link" href="professors.html">Professors</a></li>
          <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> 其他 </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#"></a> <a class="dropdown-item" href="#"></a><!drop down里的内容>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#"></a> <!drop down里的内容>
            </div>
          </li>
          <li class="nav-item"> </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
  </nav>
    <div class="container">
      <hr>
      <div class="row">
        <div class="col-6 col-lg-9">
          <h1 data_temp_dwid="1">"""
temp_begin1_2 = """</h1><!--category name-->
        </div>
        <div class="col-6 col-lg-3">
          <h></h>
			<button type="submit" id="feedbackSubmit" class="btn btn-primary btn-sm"> write review</button>
        </div>
      </div>"""
temp_end1 = """</div>
    </div>
      <hr>
      <hr>

      <footer class="text-center">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <p>HoosMyProfessor © 2018 """ + version+ """ All rights reserved.</p>
            </div>
          </div>
        </div>
      </footer>
    </div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="js/jquery-3.2.1.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap-4.0.0.js"></script>
  </body>
</html>"""
temp_begin2 = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>"""
temp_begin2_2 = """</title>
    <!-- Bootstrap -->
    <link href="css/bootstrap-4.0.0.css" rel="stylesheet">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light col-lg-12"><a class="navbar-brand" href="https://www.msnatuva.org/"><img src="LOGO.png" width="50" height="30" alt="msn logo"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active"> <a class="nav-link" href="index.html">Hoos My Professor<span class="sr-only">(current)</span></a> </li>
          <li class="nav-item"> <a class="nav-link" href="departmetnts.html">Departments</a></li>
			<li class="nav-item"> <a class="nav-link" href="professors.html">Professors<span class="sr-only">(current)</span></a></li>
          <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> 其他 </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#"></a> <a class="dropdown-item" href="#"></a><!drop down里的内容>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#"></a> <!drop down里的内容>
            </div>
          </li>
          <li class="nav-item"> </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
  </nav>
  <hr>
	  <div class="container">
	  	<div class="row">
        	<div class="col-6 col-lg-9">
         	 <h1 data_temp_dwid="1">"""
temp_end2 = """</div>
      <hr>

<hr>



    </div>
<hr>
<hr>
	<footer class="text-center">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <p>HoosMyProfessor © 2018 """ + version+ """ All rights reserved.</p><!--footer-->
            </div>
          </div>
        </div>
      </footer>
    </div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="website/js/jquery-3.2.1.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="website/js/popper.min.js"></script>
    <script src="website/js/bootstrap-4.0.0.js"></script>
</body>
</html>"""
temp_begin3 = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>"""
temp_begin3_2 = """</title>
    <!-- Bootstrap -->
    <link href="css/bootstrap-4.0.0.css" rel="stylesheet">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light col-lg-12"><a class="navbar-brand" href="https://www.msnatuva.org/"><img src="LOGO.png" width="50" height="30" alt="msn logo"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active"> <a class="nav-link" href="index.html">Hoos My Professor</a> </li>
          <li class="nav-item"> <a class="nav-link" href="departmetnts.html">Departments</a></li>
			<li class="nav-item"> <a class="nav-link" href="professors.html">Professors</a></li>
          <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> 其他 </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#"></a> <a class="dropdown-item" href="#"></a><!drop down里的内容>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#"></a> <!drop down里的内容>
            </div>
          </li>
          <li class="nav-item"> </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
  </nav>
    <div class="container">
      <hr>
      <div class="row">
        <div class="col-6 col-lg-9">
          <h1 data_temp_dwid="1">"""
temp_end3 = """<hr>
      <footer class="text-center">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <p>HoosMyProfessor © 2018 """ + version+ """ All rights reserved.</p>
            </div>
          </div>
        </div>
      </footer>
    </div>
    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="js/jquery-3.2.1.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap-4.0.0.js"></script>
  </body>
</html>"""

temp_begin4 = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>"""

temp_begin4_2 = """</title>
    <!-- Bootstrap -->
    <link href="css/bootstrap-4.0.0.css" rel="stylesheet">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light col-lg-12"><a class="navbar-brand" href="https://www.msnatuva.org/"><img src="LOGO.png" width="50" height="30" alt="msn logo"></a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"> <span class="navbar-toggler-icon"></span> </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active"> <a class="nav-link" href="index.html">Hoos My Professor<span class="sr-only"></span></a> </li>
          <li class="nav-item"> <a class="nav-link" href="departmetnts.html">Departments</a></li>
			<li class="nav-item"> <a class="nav-link" href="professors.html">Professors</a></li>
          <li class="nav-item dropdown"><a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> 其他 </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item" href="#"></a> <a class="dropdown-item" href="#"></a><!drop down里的内容>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="#"></a> <!drop down里的内容>
            </div>
          </li>
          <li class="nav-item"> </li>
        </ul>
        <form class="form-inline my-2 my-lg-0">
          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      </div>
  </nav>
    <div class="container">
      <hr>
    <div class="row">
      <div class="col-6 col-lg-10">
          <h1>"""

temp_end4 = """</div>
      <hr>

<hr>



    </div>
<hr>
<hr>
	<footer class="text-center">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <p>HoosMyProfessor © 2018 """ + version +""" All rights reserved.</p><!--footer-->
            </div>
          </div>
        </div>
      </footer>
    </div>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="website/js/jquery-3.2.1.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="website/js/popper.min.js"></script>
    <script src="website/js/bootstrap-4.0.0.js"></script>
</body>
</html>"""

def sortByNumber(list,dict):
    # takes a list of IDs and returns a sorted list of IDs based on alphabetical order of names
    temp = []
    ret = []
    for id in list:
        temp.append(dict[id])
    temp.sort(key=lambda x: x.number, reverse=False)
    for item in temp:
        ret.append(item.id)
    return ret

def sortByName(list,dict):
    # takes a list of IDs and returns a sorted list of IDs based on alphabetical order of names
    temp = []
    ret = []
    for id in list:
        temp.append(dict[id])
    temp.sort(key=lambda x: x.name, reverse=False)
    for item in temp:
        ret.append(item.id)
    return ret

def generateHTMLCategory(file,index,obj,dict,categoryInfo,classDescription):
    index.write("""<tr>
        <td class="IndexTable4"><a href="""+'"'+str(obj.id)+ '.html">' + obj.name + " - "+ categoryInfo[obj.name])
    file.write(temp_begin1 + categoryInfo[obj.name] + temp_begin1_2)
    for item in sortByNumber(obj.list_of_Class,dict):

        file.write("""      <hr>
      <div class="row">
        <div class="col-md-8 col-sm-12 col-lg-3">
          <div class="media">
		<div class="media-body">""")
        file.write('<a href="'+ str(item) +""".html"><!--href--><h5 class="mt-0">""" + dict[item].number + """</h5><!--class name-->
			""" + dict[item].name + """</a></div>
          </div>
        	</div>
        <div class="col-md-4 col-sm-12 col-lg-9">
          <div class="row justify-content-md-around m-1">

            <strong>难度:2.2 热度: 4.9</strong><br>""")
        try:
            file.write(classDescription[dict[item].number])
        except:
            print(dict[item].number + "Class Description not found")
        file.write(""""<br><!--class describtion-->

          </div>
        </div>
      </div>
      <hr>
		""")
    file.write("""<h2 class="text-center">Professors</h2>
    <hr>
  <div class="container">
      <div class="row text-center">""")
    for item in sortByName(obj.list_of_Instructor,dict):
        file.write("""<div class="col-md-4 pb-1 pb-md-0">
          <div class="card">

            <div class="card-body">""")
        file.write('<a href="'+str(item)+""".html"><h5 class="card-title">""" +dict[item].name + """</h5></a><!--href and professor name-->

            </div>
          </div>
        </div>""")
    file.write(temp_end1)

def generateHTMLClass(file,index,obj,dict,categoryInfo,classDescription):
    file.write(temp_begin2+obj.number + " - " + obj.name+temp_begin2_2)
    file.write(obj.number + " - " + obj.name + """</h1><!--class name-->
        	</div>
        <div class="col-6 col-lg-3">
          <h></h>
			<button type="submit" id="feedbackSubmit" class="btn btn-primary btn-md"> write review</button>
        </div>
      	</div>
      <hr>
      <div class="row">
        <div class="col-md-8 col-sm-12 col-lg-3">
          <div class="media">
		<div class="media-body">
          <h3 class="mt-4">Course Description</h3>
			</div>
          </div>
        	</div>
        <div class="col-md-4 col-sm-12 col-lg-9">
          <div class="row justify-content-md-around m-1">

            <br>""")
    try:
         file.write('<p>'+classDescription[obj.number])
    except:
        print(obj.number + "Class Description not found")
    file.write("""<br><!--class description-->

          </div>
        </div>
      </div>
    <hr>
    <h2 class="text-center">Sections by Instructors</h2>
    <hr>

      <div class="row text-center">""")
    for id in sortByName(obj.list_of_Section,dict):
        file.write("""<div class="col-md-4 pb-1 pb-md-0">
          <div class="card">

            <div class="card-body">
              <a href=""" + '"' + str(id)+ """.html"><h5 class="card-title">""")
        file.write(dict[dict[id].instructor].name)
        file.write("""</h5></a><!--href and professor name-->

            </div>
          </div>
        </div>""")

    file.write(temp_end2)

def generateHTMLInstr(file,index,obj,dict,categoryInfo,classDescription):
    file.write(temp_begin3 + obj.name + temp_begin3_2 + obj.name + """</h1><!--category name-->
        </div>
        <div class="col-6 col-lg-3">
          <h></h>
			<button type="submit" id="feedbackSubmit" class="btn btn-primary btn-sm"> write review</button>
        </div>
      </div>""")
    for id in sortByNumber(obj.list_of_Class,dict):
        file.write("""<hr>
      <div class="row">
        <div class="col-md-8 col-sm-12 col-lg-3">
          <div class="media">
		<div class="media-body">
          <a href=""" + '"' +str(id) + '.html"><!--href--><h5 class="mt-0">' + dict[id].number + '</h5><!--class name-->' + dict[id].name + """</a></div>
          </div>
        	</div>
        <div class="col-md-4 col-sm-12 col-lg-9">
          <div class="row justify-content-md-around m-1">

            <strong>难度:2.2 热度: 4.9</strong><br>""" )
        try:
            file.write(classDescription[dict[id].number])
        except:
            print(dict[id].number+"Class Description not found")
        file.write("""</div>
        </div>
      </div>
<hr>""")
    file.write(temp_end3)

def generateHTMLSection(file,index,obj,dict,categoryInfo,classDescription,courseURL,categoryWeb):
    file.write(temp_begin4 + obj.name + "-" + dict[obj.instructor].name + temp_begin4_2+ obj.name + "-" + dict[obj.instructor].name)
    file.write("""</h1><!--name-->
		  <a href=""" + '"' + str(obj.instructor) + """.html" ><p>"""+dict[obj.instructor].name+"""</p></a><!--instructor-->

      </div>
      <hr>
      <div class="row">
        <div class="col-md-8 col-sm-12 col-lg-12"> </div>
		  <button type="submit" id="feedbackSubmit" class="btn btn-primary btn-sm"> write review</button>
        <div class="col-md-4 col-sm-12">
          <div class="row justify-content-md-around m-1"> </div>
        </div>
      </div>
      <hr>
      <div class="row">
        <div class="col-md-6 col-sm-12">
          <h4>课程介绍</h4>

          <p>""")
    try:
        file.write(classDescription[obj.number])
    except:
        print(obj.number + "Class Description not found")
    file.write("""</p><!--课程介绍，来自course forum，不确定和sis上一样不一样-->

		<hr>
          <h7>CourseForum: </h7><a href="""+'"')
    try:
        file.write(courseURL[obj.number])
    except:
        print(obj.number + ",")
    file.write("""">Click Here</a><!--CF Link-->
			<p></p>
		<h7>Lou's List: </h7><a href="""+'"')
    try:
        file.write(categoryWeb[''.join(c for c in obj.number if c.isdigit() == False)])
    except:
        print(obj.number + "Category Info not found")
    file.write("""">Click Here</a><!--Lou link-->

        </div>
        <div class="col-md-6 col-sm-12">
          <h2>Rating</h2>
          <hr>
          <div class="progress mt-4" lang="zh">
            <div class="progress-bar bg-success" role="progressbar" aria-valuenow="21.5" aria-valuemin="0" aria-valuemax="100" style="width: 21.5%"> 难度：2.2</div>
          </div>
          <div class="progress mt-4" lang="zh">
            <div class="progress-bar bg-danger" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: 98%"> 热度：4.9</div>
          </div>""")
    temp = obj.comments
    temp.sort(key = len, reverse= True)
    first = True
    for comment in temp:
        if first:
            first = False
            file.write("""</div>
      </div>
      <hr>
<hr>

      <div class="row">
        <div class="col-md-6 col-sm-12 col-lg-12">
          <div class="row">
            <div class="col-5">
              <h4>Reviews:</h4>
            </div>
            <div class="col-5"> </div>
            <div class="col-5" lang="zh">
              <h5>难度: 1</h5>
            </div>
            <div class="col-6 offset-lg-1" lang="zh">
              <h5 class="text-left"><span aria-hidden="true"></span> 热度: 5</h5>
            </div>
          </div>
          <h5><span class="badge badge-secondary"></span></h5><!--以后可以加入tag-->
          <p>""")
            file.write(comment)
            file.write("""</p><!--评价内容-->
 			<hr>
			<hr>
		</div>""")
        else:
            file.write("""<div class="col-md-6 col-sm-12 col-lg-12" lang="zh">
          <div class="row">
            <div class="col-5">
              <h5>难度: 3</h5>
            </div>
            <div class="col-6 offset-lg-1">
              <h5 class="text-left"><span aria-hidden="true"></span>热度: 4</h5>
            </div>
          </div>
          <h5><span class="badge badge-secondary"></span></h5><!--tag-->
          <p>""")
            file.write(comment)
            file.write("""</p><!--评价内容-->
			<hr>
			<hr>
        </div>""")
    file.write(temp_end4)
