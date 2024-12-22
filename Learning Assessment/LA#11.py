class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
   
       
    def describePhone(self):
        print(f" My phone brand is {self.brand}. And the model is {self.model}")
   
   
class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
       
oppoF11pro = Android("oppof11pro", "Oppo")      
oppoF11pro.describePhone()
