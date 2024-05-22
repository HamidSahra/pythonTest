# شی گرایی  object oriented
# حرف اول نام کلاس باید بزرگ باشد. مهم مهم مهم

# class MyClass:
#     x = 5   # this is a property  
#     y = 11
    
# p1 = MyClass()
# p2 = MyClass()

# print(p1.x)
# print(p2.x)    
# print(p1.y)


# class MyClass:
#     def __init__(self, name, lastname, age):
#         self.myname = name
#         self.mylastname = lastname
#         self.myage = age
        
# p1 = MyClass("amir", "amiri", 45)
# p2 = MyClass("reza", "mousavi", 54)

# print(p1.myname)
# print(p2.mylastname)
# print(p1.myage)


# class Person:
#     def __init__(self):
#         print("hello from init")
        
# p1 = Person()
# p2 = Person()
        
        
# class Person:
#     def fullname(self):
#         print("hello from fullname function")
        
# p1 = Person()
# p1.fullname()


# class Person:
#     def __init__(self, name, lastname):
#         self.myname = name
#         self.mylastname = lastname
        
#     def fullname(self):
#         print(f"hey I am {self.myname} {self.mylastname}")
# p1 = Person("milad", "miladi")
# p1.fullname()



# class Person:
#     def __init__(self, name, lastname, age):
#         self.myname = name
#         self.mylastname = lastname
#         self.myage = age
        
#     def fullname(self):
#         print(f"my name is {self.myname} {self.mylastname} and my age is {self.myage}")
            
# p1 = Person("milad", "miladi", 29)

# # print(p1.myname)
# # print(p1.mylastname)
# # print(p1.myage)
# p1.fullname()

# p1.myname = "reza"
# p1.mylastname = "moosavi"

# del p1.myage
# p1.fullname()



class Car:
    cars_number = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.status = False
        # print(f"Hi, Im from {self.name}")
        Car.cars_number += 1
        
    def start(self):
        if self.status == False:
            self.status = True
            print(f"{self.name} is starting")
        else:
            print("car is on dont start please")
    
        
        
    def off(self):
        if self.status:
            self.status = False
            print(f"{self.name} is off now")
        else:
            print("car is off please start first")
       
# print(Car.cars_number) 
car1 = Car("benz", "250000")
car2 = Car("pegeut", "120")
car3 = Car("bmw", "190000")
# print(Car.cars_number)

# print(car3.name)
# car3.name = "pride"
# print(car3.name)

# car1.start()
# car1.start()
# car1.off()
# car1.off()
# print(car1.status)
# print(Car.cars_number)

car3.cars_number = 5
# print(car3.cars_number)

Car.cars_number = 9
print(Car.cars_number)
print(car1.cars_number)
print(car2.cars_number)
print(car3.cars_number)
