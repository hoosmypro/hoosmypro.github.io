Format:
Object: Category
>Fields:
>+ id:int          (a six digit int, begins with 1, e.g. 100001)
>+ name:string     (e.g. "CS")
>+ list_of_Class:list        (id(s) of classes this category has e.g. [200001,200002])
>+ list_of_Instructor:list   (id(s) of instructors this category has e.g. [300003,300004])

Object: Class
>Fields;
>+ id:int           (a six digit int, begins with 2, e.g. 200001)
>+ number:string    (e.g. "CS2150")
>+ name:string      (e.g. "Introduction to Programming")
>+ list_of_Instructor:list   (id(s) of instructors who teach this class e.g. [300003,300004])
>+ list_of_Class:list        (id(s) of sections this class has e.g. [400001,400002])

Object: Instructor
>Fields;
>+ id:int           (a six digit int, begins with 3, e.g. 300001)
>+ name:string      (e.g. "David Edwards")
>+ list_of_Class:list        (id(s) of classes he/she teaches e.g. [200001,200002])

Object:Section
>Fields;
>+ id:int           (a six digit int, begins with 2, e.g. 400001)
>+ number:string    (e.g. "CS2150")
>+ name:string      (e.g. "Introduction to Programming")
>+ comments:string  (e.g. "This is an interesting class")
>+ instructor:int   (e.g. who teaches this class, represented by his/her id e.g. 200001)
>+ belonged:int     (e.g. what class this section belongs to, represented by his/her id e.g. 300001)
