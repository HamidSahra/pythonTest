# class Person:  #parent
#     def __init__(self, firstname, lastname):
#         self.fname = firstname
#         self.lname = lastname
        
#     def printname(self):
#         print(self.fname, self.lname)
        
        
# # p1 = Person("amir", "amiri")
# # print(p1.fname)
# # p1.printname()

# # class Student(Person): #child  #ارث بری در پایتون
# #     pass

# # s1 = Student("hamid", "hamidi")
# # print(s1.lname)
# # s1.printname()


# # بازنویسی تابع __init__

# class Student(Person): #child
#     def __init__(self, firstname, lastname, age):
#         # Person.__init__(self, firstname, lastname)
#         super().__init__(firstname, lastname)
#         # خط27 همان کار خط26 را انجام میدهد. 
#         #نماینده و جانشین کلاس پرنت یا پدر است.
#         # در واقع در اینجا super  همان Person است.
#         self.age = age
        
#     def printage(self):
#         print(f"age is {self.age}")
        
# s1 = Student("hamid", "hamidi", 45)
# print(s1.age)

# s1.printage()