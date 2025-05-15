
class Dog:

    def __init__(self, color, raza):
        
        self.color = color
        self.raza = raza

    def say_color(self):
        print("my color is: ", self.color)

        

my_dog = Dog("amarillo")

my_dog.say_color()


