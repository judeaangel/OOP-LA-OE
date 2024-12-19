class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, function_name):
        def wrap(*args, **kwargs):
            print("Introducing...")
            function_name(*args, **kwargs)
            print(f"this character is amazing!")
        return wrap
       
char = AnimeCharacter("Sukuna","King of Curses")

@char.introduce
def character_intro():
    print(f"I am {char.name} and I can use {char.ability}")
character_intro()
