class Cat:
    
    def __init__(self, color):
        
        self.color = color

    def say_color(self):
        print("my color is: ", self.color)
        

my_dog = Cat("calico")

my_dog.say_color()


