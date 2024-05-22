
# def myfunc(a):
#     return a + 10

# myfunc2 = myfunc
# print(myfunc2(20))



# x = lambda a : a + 10
# print(x(32))

# m = lambda a, b, c : a + b + c

# print(m(12, 17, 70))


# def myfunc(n):
#     def new(a):
#         return n * a
    
#     return new

# mydoubler = myfunc(2)
# print(mydoubler(4))

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(3)
print(mydoubler(5))