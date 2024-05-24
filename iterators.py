
# mylist = ['amir', 'ali', 'reza', 'farid', 'hamid'] #iterable

# myiterator = iter(mylist)  #iterable =====> iterator

# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))

# for name in mylist:
#     print(name)

# name = "hamidsahranavard"  #iterable
# myit = iter(name)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# for n in name:
#     print(n)

# ساخت ایتربل شخصی - make personal iterable

class Myiter:
    
    def __init__(self,number):
        self.number = number
        
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= self.number:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
        
    
o1 = Myiter(8)
# myiterator = iter(o1)

# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))

for n in o1:
    print(n)