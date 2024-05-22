#تمرین
# تعریف دسترسی های یوزرهای یک سایت 


cs = [
    {
        "title": "python",
        "teacher": "amiri"
    },
    {
        "title": "html",
        "teacher": "dehyami"
    },
    {
        "title": "php",
        "teacher": "enayati"
    }
]



class User:  #parent
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
    
    def fullname(self):
        print(f"my fullname is {self.fname} {self.lname}")
        
class Student(User):  #child
    def __init__(self, firstname, lastname, email):
        super().__init__(firstname, lastname)
        self.email = email
        self.courses = []
        
    def fullname(self):
        print("I am an student")
        super().fullname()
        
    def printcourses(self):
        if self.courses:
            for course in self.courses:
                print(course['title'])
        else:
            print('this user has no courses')

class Teacher(User):
    def __init__(self, firstname, lastname, code):
        super().__init__(firstname, lastname)
        self.code = code
        
    def fullname(self):
        print("I am a teacher")
        super().fullname()
        
s1 = Student("hamid", "sahra", "hamid@gmail.com")

s1.courses.append(cs[1])
s1.courses.append(cs[0])

# print(s1.courses)
s1.printcourses()

s2 = Student("javid", "janam", "javid@gmail.com")
s2.printcourses()