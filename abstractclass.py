from abc import ABC, abstractmethod, abstractproperty

class Animal(ABC):
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractproperty
    def legs(self):
        pass
    
    
class Lion(Animal):
    def move(self):
        print('lion is moving')