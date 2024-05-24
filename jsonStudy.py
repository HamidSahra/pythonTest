
import json
# x = '{ "name":"John", "age":30, "city":"New York", "isTeacher": true, "lastname": null}'
# # print(x)
# y = json.loads(x)

# print(y['lastname'])

# r = json.dumps(True)

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York",
#   "isTeacher": True,
#   "lastname": None
# }

# y = json.dumps(x)
# print(y)
# print(type(y))


# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# y = json.dumps(x)
# print(type(y))

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["city"])