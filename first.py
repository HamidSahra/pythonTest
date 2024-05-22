# print("Hello World!") #first code!


# import sys       # check the python version of the editor
# print(sys.version)

# import mymodule
# mymodule.greeting("Hamid")

# if 5 > 2:
#     print("Five is greater than two!")


# print(type('hello word'))  # this is an string
# print('---------------------')
# print(type(180))
# print('---------------------')
# print(type(75.5))
# print('---------------------')
# print(type(65j))
# print('---------------------')
# print(142/4)
# txt= " my nane is Hamid Im from tehran "
# txt_length=len(txt)
# print(txt_length)
# print(txt.count(" "))

# x = int("4")
# print(x)
# y = float("3")
# print(y)
# print("she is called 'Foroogh'")
# print('He is called "ali"')

# a = "python is the best"
# print(a[5])
# print(len(a))

# for x in "python":
#     print(x)

# txt = " in the name, of god, the compationed, the mercyful, "
# if "name" in txt:
#     print("yes, 'god' is present")
# else:
#     print("no, i am so sory")
# if "eblis" not in txt:
#     print("No, I am So sory")

# print(txt[9:19])
# print(txt.upper())
# print(txt.lower())
# print(txt.strip())
# print(txt.replace("g", "G"))
# print(txt.replace("i", "I"))
# print(txt.split(","))

# x = "Hamid is"
# y = "good Man"
# z = x + " " + y
# print(z)

# age = 44
# txt = f"My name is Hamid, I am {age}"
# print(txt)

# price = 66
# txt = f"The price is {price} dollars"
# print(txt)
# txt = f"The price is {price:.2f} dollars"
# print(txt)
# txt = f"The price is {15 * 5} dollars"
# print(txt)

# txt = "We are so-called \"Shomali\" frome the north of Iran"
# print(txt)
# txt = 'It\'s all right'
# print(txt)
# txt = "i am from \\ rasht"
# print(txt)
# txt = "I am from Rasht\nI live in Tehran"
# print(txt)
# txt = "Hello\rWorld!"
# print(txt)
# txt = "Hello\teverybode"
# print(txt)
# txt = "Hello\beverybode"
# print(txt)
# txt = "Hello\feverybode"
# print(txt)
# txt = "\x48\x32\x8b\x64\x16c"
# print(txt)

# txt = "hamid sahranavard"
# x = txt.capitalize()
# print(x)
# txt = "HAMID Sahranavard"
# x = txt.casefold()
# print(x)
# txt = "hamid sahranavard"
# x = txt.center(50)
# print(x)
# txt = "hamid sahranavard"
# x = txt.count("sahranavard")
# print(x)
# txt = "hamid sahranavard"
# x = txt.encode()
# print(x)
# txt = "hamid sahranavard."
# x = txt.endswith(".")
# print(x)

# a = 200
# b = 22
# if b>a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")

# print(bool("Hamid"))
# print(bool(-15))

# class myclass():
#     def __len__(self):
#         return 0
# myobj = myclass()
# print(bool(myobj))  # the answer is False

# x = 200
# print(isinstance(x, int))

list1 = ["i", "you", "us", "We", "They", "He", "It"]
list2 = ["we", "you", "they"]
tuple1 = ("he", "she", "it")
# list1.insert(2, "your")
# list1[0:1] = ["i", "they", "thay"]
# list1[1] = "she"
# print(list1)
# list1.append("he")
# print(list1)
# list1.extend(list2)
# list1.extend(tuple1)
# print(list1)
# list1.remove("you")
# list1.pop(1) #remove index 1 , If you do not specify the index, the pop() method removes the last item.
# del list1[2]
# del list1  #The del keyword can also delete the list completely.
# list1.clear()  # The list still remains, but it has no content.

# for x in list1:
#     print(x)

# for i in range(len(list1)): # You can also loop through the list items by referring to their index number.
#     print(list1[i])

# i = 0
# while i<len(list1):
#     print(list1)
# i = i + 1

# [print(x) for x in list1]

# newlist = []
# for x in list1:
#     if "s" in x:
#         newlist.append(x)
#         print(newlist)

# newlist = [x for x in list1 if "u" in x]
# print(newlist)

# list1.sort()
# print(list1)
# list1.sort(reverse = True)
# print(list1)
# list1.sort(key = str.lower)
# list1.reverse()
# print(list1)

num1 = [100, 21, 67, 6, 90, 56, 42, 13]
# num1.sort()
# print(num1)
# num1.sort(reverse = True)
# print(num1)

# mylist = list1.copy()
# print(mylist)
# mylist = list(list1) #another way to copy a list
# print(mylist)

# list3 = list1 + num1
# print(list3)

# for x in num1:
#     list1.append(x)
#     print(list1)


# tuple1 = ("i", "you", "us", "We", "They", "He", "It")
tuple1 = tuple(("i", "you", "us", "We", "They", "He", "It"))
# print(tuple1)
tuple2 = (100, 21, 67, 6, 90, 56, 42, 13, 100, 90, 90)
# print(type(tuple2))

# list1 = list(tuple1)
# list1[0] = "me"
# tuple1 = tuple(list1)
# print(tuple1)

# list1 = list(tuple1)
# list1.append("me")
# tuple1 = tuple(list1)
# print(tuple1)

# y = ("those", )
# tuple1 += y
# print(tuple1)

# list1 = list(tuple1)
# list1.remove("i")
# tuple1 = tuple(list1)
# print(tuple1)

# del tuple1
# print(tuple1)

# cloths = ("shirt", "Tshirt", "hodi")
# (blue, red, green) = cloths
# print(blue)
# print(red)
# print(green)

cloths = ("shirt", "Tshirt", "hodi", "scarf", "hat", "shoe", "coat")
# (blue, *red, green) = cloths
# print(blue)
# print(red)
# print(green)

# for x in cloths:
#     print(x)

# for i in range(len(cloths)):
#     print(cloths[i])

# for i in range(5, 31, 5):
#     print(i)

# i = 0
# while i< len(cloths):
#     print(cloths[i])
#     i = i+1

# tuple3 = tuple1 + cloths
# print(tuple3)

# tuple3 = cloths * 3
# print(tuple3)

# x = tuple2.count(90)
# print(x)

# x = tuple2.index(13)
# print(x)

# x = cloths.index("shoe")
# print(x)

set1 = {"shirt", "Tshirt", "hodi", "scarf", "us", "We"}
# set1 = set(("shirt", "Tshirt", "hodi", "scarf"))
# print(set1)
# print("hodi" in set1)    #True or False
# print("shoe" not in set1)  #True or False

# set1.add("shoe")
# print(set1)
set2 = {"you", "us", "We", "They", "Tshirt", "hodi"}
# set1.update(set2)
# print(set1)

# set1.remove("hodi")
# set1.discard("scarf")
# print(set1)

# x = set1.pop() #when using the pop() method, you do not know which item that gets removed.
# print(x)
# print(set1)

# set1.clear()  #The clear() method empties the set
# print(set1)

# del set1  # The del keyword will delete the set completely
# print(set1)

# for x in set1:
#     print(set1)

# set3 = set1.union(set2) #returns a new set with all items from both sets
# set3 = set1 | set2 #You can use the | operator instead of the union() method, and you will get the same result.
set3 = {1, 2, 3, 4, "We", "They", "Tshirt", "hodi"}
# print(set3)
# set4 = set1.union(set2, set3) #Join Multiple Sets
# set4 = set1 | set2 | set3  #Join Multiple Sets
# print(set4)

tuple1 = (5, 6, 12, 15, 21, "We", "They")
# set11 = set1.union(tuple1)  # Join a Set and a Tuple
# print(set11)

# set1.update(set2)
# set1.union(set2)  #Both union() and update() will exclude any duplicate items.
# print(set1)

# set3 = set1.intersection(set2) #keep only the duplicates
# set3 = set1 & set2 #You can use the & operator instead of the intersection() method
# set3 = set1.intersection(tuple1)
# print(set3)

# set1.intersection_update(set2)
# print(set1)

# set3 = set1.difference(set2) #will return a new set that will contain only the items from the first set that are not present in the other set.
# set3 = set1 - set2 #You can use the - operator instead of the difference() method
# print(set3)

# set1.difference_update(set2)
# print(set1)

# set3 = set1.symmetric_difference(set2) #will keep only the elements that are NOT present in both sets
# set3 = set1 ^ set2  #You can use the ^ operator instead of the symmetric_difference() method
# set3 = set1.symmetric_difference(tuple1)
# print(set3)

# set1.symmetric_difference_update(set2)
# print(set1)

dict1 = {"i": "we", "you": "your", "it": "they", "year": "1980", "married": "False"}
# dict1 =dict(i= "we", you = "you", it = "they", year = 1980, married = False)

# print(dict1)
# print(type(dict1))
# print(dict1["you"])
# print(len(dict1))

# x= dict1["it"]
# x = dict1.get("i")
# print(x)
# x = dict1.keys()
# print(x)
# dict1["us"] = "our"
# print(x)
# x = dict1.values()
# print(x)
# dict1["year"] = 2024
# print(x)
# x = dict1.items()   #Get a list of the key:value pairs
# print(x)

# if "it" in dict1:
#     print("yes, 'it' is one of the keys")

# dict1["you"] = "yours"
# dict1["us"] = "ours"
# print(dict1)

# dict1.update({"year": 1359})
# dict1.update({"tehrancoming": 1378})
# print(dict1)

# dict1.pop("us")
# print(dict1)

# dict1.popitem() #The popitem() method removes the last inserted item
# print(dict1)

# dict1.clear()
# print(dict1)

# del dict1
# print(dict1)

# for x in dict1: #Print all key names in the dictionary, one by one
#     print(x)

# for x in dict1:  #Print all values in the dictionary, one by one
#   print(dict1[x])

# for x in dict1.values(): #You can also use the values() method to return values of a dictionary
#     print(x)

# for x in dict1.keys(): #You can use the keys() method to return the keys of a dictionary
#     print(x)

# for x, y in dict1.items(): #Loop through both keys and values, by using the items() method
#     print(x, y)

# dict2 = dict1.copy()
# dict2 = dict(dict1)  #Make a copy of a dictionary with the dict() function
# print(dict2)

# child1 = {
#     "name" : "jane",
#     "year" : "1995"
# }
# child2 = {
#     "name" : "james",
#     "year" : "1998"
# }
# child3 = {
#     "name" : "josep",
#     "year" : "2000"
# }

# mychilds = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3
# }
# print(mychilds)

mychilds = {
    "child1": {"name": "emili", "year": 2001},
    "child2": {"name": "joe", "year": 2005},
    "child3": {"name": "andro", "year": 2008},
}
# print(mychilds)
# print(mychilds["child3"]["name"])

# for x, obj in mychilds.items():
#     print(x)
#     for y in obj:
#         print(y + ":", obj[y])

# a = 3
# b = 340
# print("A") if a>b else print("B")

# print("A") if a>b else print("=") if a==b else print("B")



import json

x =  '{ "name":"John", "age":30, "city":"New York", "isTeacher": true, "lastname": null}'
print(x)

x = json.loads(x)