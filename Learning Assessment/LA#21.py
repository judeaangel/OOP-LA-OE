class HaloHalo:
    def __init__(self, banana, ube, langka):
        self.__banana = banana
        self.__ube = ube
        self.__langka = langka

    def __str__(self):
        return f"My Halo-Halo has {self.__banana}, {self.__ube}, and {self.__langka}"

    def may_banana_ba(self, sweetness):
        if sweetness <= 100:
            return self.__banana
        else:
            return "Secret"

    def i_set_to(self, bagong_banana):
        self.__banana = bagong_banana


halo_halo = HaloHalo("sliced banana", "ube halaya", "langka strips")
halo_halo.i_set_to("hiniwang saging na saba")
print(halo_halo.may_banana_ba(50))
