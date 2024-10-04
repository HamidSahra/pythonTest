
# # def hello(name):
    
# #     def hello_name():
# #         print(f'hello {name}')
        
# #     return hello_name

# # new = hello("hamid")

# # new()


# # # decorator
# # def hello_decorator(func):
    
# #     # wraper
# #     def inner():
# #         print("Hello, this is before function execution")
# #         func()  # hi user
# #         print("this is after function execution")
        
# #     return inner

# # @hello_decorator
# # def hello():
# #     print("hi user")
    
# # hello()
    
# # hello = hello_decorator(hello)

# # hello()



# # decorator
# def hello_decorator(func):
    
#     # wraper
#     def inner(name):
#         print("Hello, this is before function execution")
#         func(name)  # hi user
#         print("this is after function execution")
        
#     return inner

# @hello_decorator
# def hello(name):
#     print(f"hi {name}")
    
# hello("hamid")




# # decorator
# def hello_decorator(func):
    
#     # wraper
#     def inner(*args, **kwargs):
#         print("Hello, this is before function execution")
#         func(*args, **kwargs)  # hi user
#         print("this is after function execution")
        
#     return inner

# @hello_decorator
# def hello(name, lastname):
#     print(f"hi {name} {lastname}")
    
# hello("hamid", "sahra")



# def updecorator(func):
#     def inner(*args, **kwargs):
#         x = func(*args, **kwargs)
#         return x.upper()
#     return inner

# @updecorator
# def test(name):
#     return f"hello {name}"

# # print(test('hamid'))

# x = test("hamid")
# print(x)





# import time

# def calculate_time(func):
#     def inner(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f"total time: {end - begin}")
#     return inner

# @calculate_time
    
# def test(name):
#     time.sleep(4)
#     print(f"hello {name}")
    
# test('hamid')



def dec1(func):
    def inner():
        x = func()
        return x * 3
    return inner

def dec2(func):
    def inner():
        x = func()
        return x * 10
    return inner

@dec1
@dec2
def test():
    return 5

print(test())