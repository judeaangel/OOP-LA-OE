class Appliance:
    def __init__(self, name):
        self.name = name
    def operate(self):
       print("Operating!")
       
class WashingMachine(Appliance):
    def operate(self):
      print(f"{self.name}: Washing Clothes")

class Regrigerator(Appliance):
    def operate(self):
        print(f"{self.name}: Keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print(f"{self.name}: Heeting food!")

washingmachine = WashingMachine("washing machine")
refrigerator = Regrigerator("refrigerator")
microwave = Microwave ("microwaver")

def tawaginSila(appliances):
    appli.operate()
   
for appli in [washingmachine, refrigerator, microwave]:    
   tawaginSila(appli)
