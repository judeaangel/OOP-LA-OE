class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
 
       
class Fish(Animal):    
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = can_swim
       
Fish = Fish("Tilapia", "Fish", True)    
print(Fish.can_swim)
