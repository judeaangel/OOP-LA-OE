class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
       
    def describeVehicle(self):
        print(f" my car brand is {self.brand}. And the model is {self.model}, with {self.fuel_type} fuel type")
   
   
class Car(Vehicle):
      pass
   
chevrolet = Car("Chevrolet", "Sedans", "Diesel")
chevrolet.describeVehicle()

class Motorcycle(Vehicle):
      pass
   
Honda = Motorcycle("Honda", "Click", "Electric")
Honda.describeVehicle()
