
class Dog:
    
    def __init__(self, raza):
        
        self.raza = raza

    def say_color(self):
        print("my raza is: ", self.raza)
        

my_dog = Dog("amarillo")

my_dog.say_color()


