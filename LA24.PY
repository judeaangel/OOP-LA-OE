from abc import ABC, abstractmethod
class GameCharacter(ABC):
      @abstractmethod
      def attack(self):
          pass
     
class Warrior(GameCharacter):
     def attack(self):
         print("Swings Sword!")
         
class Mage(GameCharacter):
     def attack(self):
         print("\nCasts a Fireball!")      
         
class Archer(GameCharacter):
     def attack(self):
         print("\nShoots and arrow!")    
         
GameCharacter = Warrior()
GameCharacter.attack()        
         
GameCharacter = Mage()
GameCharacter.attack()

GameCharacter = Archer()
GameCharacter.attack()  
