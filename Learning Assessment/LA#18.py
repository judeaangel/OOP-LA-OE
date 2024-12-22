class halo_halo:
    def __init__(self, banana, ube, langka):
        self.__banana = banana
        self.__ube = ube
        self.__langka = langka
       
    def __str__(self):
        return f"Halo-halo is my favorite dessert food of all time. Especially the {self.__banana}, {self.__ube}, and {self.__langka} there? It's so good!"
       
       
halohalo = halo_halo("banana", "ube", "langka")
print(halohalo)
