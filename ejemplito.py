
class Dog:
    
    def __init__(self, color):
        
        self.color = color

    def say_color(self):
        print("my color is: ", self.color)
        

my_dog = Dog("amarillo")
my_dog_red = Dog("red")

my_dog.say_color()


