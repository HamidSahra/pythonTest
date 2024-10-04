
# first class function in python

# Safely open the file

# file = open("hello.txt", "w")



# try:

#     file.write("Hello, World!")

# finally:

#     # Make sure to close the file after using it

#     file.close()


def test(func):
    return func

def test2(number):
    print(number + 5)
    
a = test(test2)
a(7)

mylist = [test2]
print(mylist)