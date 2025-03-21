"""This is a "self" example with cats. To run this, you will only need one thing:
 Python.
 If you have that, then you are ready to run this code. This code will teach you how to use classes, how to define, and use self the appropriate way.
 """



class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def purr(self):
        print(f"{self.name} - purr")

    def change_name(self, new_name):
        self.name = new_name

cat = Cat("Spiral", "American Shorthair")

cat.purr()

cat.change_name("Clusky")

cat.purr()