# def my():
#     print('Hello')
    
# my()

# def my_name(name, lastname):
#     print(f"hello {name} {lastname}")
#     print(f"how are you {name} {lastname}?")
# my_name(name = "amir", lastname = "amiri")
# my_name("amir", "amiri")

# def sum(a, b):
#     print(a + b)
    
# sum(2, 4)

# def hello(name1, name2):
#     print(f"hello {name1}")
#     print(f"hello {name2}")
# hello("ali", "sahar")

# def hello(*names):
#     print(names)
#     print(f"hello {names}")
# hello("amir", "ali", "hamed", "farid", "mehdi", "reza")

# def hello(*names):
#     for name in names:
#         print(f"hello {name}")
        
# hello("amir", "ali", "hamed", "farid", "mehdi", "reza")

# def hello(fname, lname, *args, **kwargs):
#     print(f"my name is: {fname}")
#     print(f"my last name is: {lname}")
#     print(args)
#     print(kwargs)
# hello("hamid", "Sahranavard", "ali", "omid", "hamed", From = "Tehran", age = 44)



# def me(lname, name = "amir"):
#     print(f"my name is {name} {lname}")
    
# me("amiri", "reza")

# def hello(b):
#     for item in b:
#         print(f"hello {item}")
        
# mylist = {"amir", "ali", "farid", "hasan"}
# # mylist = {
# #     "name": "hamid",
# #     "from" : "tehran",
# #     "age" : 45
# # }
# hello(mylist)
# print(type(mylist))

# hello("hamid")


# def sum(a, b):
#     c = a + b
#     return c
# # sum(12, 5)
# # print(sum(12, 5))
# result = sum(12, 5)
# print(result)

# def sum(a, b):
#     return a + b
# result = sum(12, 5)
# print(result + 6)


# def sum(a, b):
#     a += 1
#     b += 5
#     c = 16
#     return a, b, c 
# result = sum(12, 5)
# # print(result)  #or
# # for item in result:
#     # print(item)   # or
# print(result)


# username = input("enter your username: ")
# def validation(username):
#     if len(username) > 8:
#         return False
#     else:
#         return True
# if validation(username):
#     print("your username is ok")
# else:
#     print("your username is wrong!!!")




# def myfunc(name):
#     ups = 0
#     lows = 0
#     for n in name:
#         if n.isupper():
#             ups += 1
#         elif n.islower():
#             lows += 1
            
#         else:
#             pass
#     print(f"upper cases: {ups}")
#     print(f"lower cases: {lows}")
    
# while True:
#     name = input('enter your name: ')
#     myfunc(name)

# def numbertype(number):
#     if number % 2 == 0:
#         print('this is an even number')
#     else:
#         print('this is an odd number')

# while True:
#     number = int(input("enter a number: "))
#     # numbertype(number)




# def converter(day, month, year):
#     if month >10 or day > 10 and month == 10:
#         birthday = year + 622
#     else:
#         birthday = year + 621
        
#     print(f"your year of birthday is {birthday}") 
    
# day = int(input("enter day: "))
# month = int(input("enter month: "))
# year = int(input("enter year: "))

# converter(day, month, year)
 
 
 
# def myfunc(a):
#     return a + 10

# myfunc2 = myfunc
# print(myfunc2(20))



# def myfunc():
#     print("Hello from a function")
# myfunc()


#Information can be passed into functions as arguments
# def myfunc(fname):
#     print(fname + " sahra")
# myfunc("hamid")
# myfunc("abo")
# myfunc("Javid")
# myfunc("Somi")


# def myfunc(fname, lname):
#     print(fname + " " + lname)
# myfunc("hamid", "Sahra")
# myfunc("abo", "sahra")
# myfunc("Javid" , "Sahra")
# myfunc("Somi", "sahra")


# def myfunc(*kids):
#     print("The youngest child is " + kids[1])
# myfunc("emil", "tobias", "linus")


# def myfunc(child2, child1, child3):
#     print("The older child is " + child1)
# myfunc(child3 = "abi", child2 = "aboo", child1 = "hamid")


# def myfunc(**kwargs):
#     print("his last name is " + kwargs["lname"])
# myfunc(fname = "Hamid", lname = "sahra")


# def myfunc(country = "IRAN"):
#     print("I am from " + country)
# myfunc()
# myfunc("Sweden")
# myfunc("USA")
# myfunc("Brazil")


# def myfunc(food):
#     for x in food:
#         print(x)
        
# fruits = ["apple", "banana", "cherry"]
# myfunc(fruits)


# def myfunc(x):
#     return 4 * x
# print(myfunc(3))
# print(myfunc(1))
# print(myfunc(9))


# def myfunc():
#     pass

# def myfunc(x, /):
#     print(x)
# myfunc(4)

# def myfunc(x):
#     print(x)
# myfunc(x =3)


# def myfunc(*, x):
#     print(x)
# myfunc(x = 4)

# def myfunc(*, x):
#     print(x)
# myfunc(3)


# def myfunc(a, b, /, *, c, d):
#     print(a + b + c + d)
# myfunc(3, 4, c = 8, d = 5)


def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(7)