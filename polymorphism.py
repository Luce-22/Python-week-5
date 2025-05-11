class Frog:
    def move(self):
        print("Hopping on the lillies")

class Lion:
    def move(self):
        print("Running through the savannah")

class Bat:
    def move(self):
        print("Flying through the air")

class Horse:
    def move(self):
        print("Galloping in the field")

# Creating a list of different animals
animals = [Frog(), Lion(), Bat(), Horse()]

# Demonstrating polymorphism
for animal in animals:
    animal.move()