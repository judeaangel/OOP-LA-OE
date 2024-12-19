class party:
    def __init__(self, theme, foods, dish, secret):
        self.theme = theme
        self.foods = foods
        self.dish = dish
        self.secret = secret
   
       
    def show_foods(self):
        print("Theme:", self.theme)
        print("Foods:", self.foods)
        print("Dish:", self.dish)  
        self.__priv()
       
    def __priv(self):
        print("secret:", self.secret)

halloween_party = party("Halloween Party", "Eyeball Pasta", "Mini Pumpkin Pies", "Caviar")
birthday_party = party("Birthday Party", "Shanghai", "Spaghetti", "Lechon")

halloween_party.show_foods()
birthday_party.show_foods()
