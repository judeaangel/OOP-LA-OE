class halo_halo:
    def __init__(self, banana, ube, langka):
        self.__banana = banana
        self.__ube = ube
        self.__langka = langka
   
       
    def __str__(self):
        return f"Halo-halo is my favorite dessert food of all time. Especially the {self.__banana}, {self.__ube}, and {self.__langka} there? It's so good!"
       
    def may_ube_ba(self, age):
            return "Secret"
       
    def i_set_to(self, bago, nanay_ka_ba):
        if nanay_ka_ba == "oo":
            self.uber = bago
        else:
            print("secret")
       
halohalo = halo_halo("banana", "ube", "langka")

halohalo.i_set_to("buong uber", "oo")
print(halohalo.may_ube_ba(31))
