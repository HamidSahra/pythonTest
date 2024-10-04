
class Person:
    def __init__(self):
        self.a = 7   #public
        self._b = 15  #protected
        self.__c = 19   #private #فقط درون این کلاس اجازه دسترسی داریم
        
    def test(self):
        print(self.__c)
        
        
p1 = Person()

p1.__c = 20
print(p1.__c)

p1.test()