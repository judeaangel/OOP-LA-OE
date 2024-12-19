class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price
   
       
    def describeToy(self):
        print(f" The name of my toy is {self.name}. And the price is {self.price}!! Amaaazinggggggggggggggggg!!")
   
   
class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
       
Dolls = Toy("Pawpaw", "₱1,000,000")      
Dolls.describeToy()
