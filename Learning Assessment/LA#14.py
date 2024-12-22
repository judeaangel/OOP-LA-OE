class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    def describeSpiderman(self):    
        print(f"{self.name} {self.age}")
       
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
           
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
       
Tom = Tom("Tom", 28, "Spider-Man No Way Home")
Tobey = Tobey("Tobey", 49, "Spider-Man")
Andrew = Andrew("Andrew", 41, "The Amazing Spider-Man")      

print(Tobey.name.upper(),Tobey.movieTitle.upper())
print(Andrew.name.upper(),Andrew.movieTitle.upper())
print(Tom.name.upper(),Tom.movieTitle.upper())
