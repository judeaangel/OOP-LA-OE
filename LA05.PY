class hero():
    def __init__(self, name, role, dmg_type):
       self.name = name
       self.role = role
       self.dmg_type = dmg_type
       
    def __str__(self):
        return f"{self.name} is a {self.role} hero with {self.dmg_type} power."
       
hero1 = hero("Miya", "Marksman", "attack damage")  
hero2 = hero("Kagura", "Mage", "magic damage")  
hero3 = hero("Xborg", "Fighter", "attack damage")  
hero4 = hero("Natalia", "Assasin", "attack damage")
hero5 = hero("Rafaela", "Marksman", "magic damage")
print(hero)
