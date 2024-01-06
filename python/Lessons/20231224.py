# base class / parent class (the class which inherits) / superclass

# child class (the class which inherits)

class Animal:
    cool = True  # class att.

    # species
    # name
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):  # instance method
        print(f"this animal says {sound}")

    def __repr__(self):
        return f"{self.name} is a {self.species}"


class Cat(Animal):  # child class / subclass
    # def __init__(self, name, species, breed, toy):
    def __init__(self, name, breed, toy):
        # Animal.__init__(self, name, species)
        super().__init__(name, species="cat")
        self.breed = breed
        self.toy = toy


# blue = Cat("Bob", species="Cat", breed="dog", toy="string")
blue = Cat(name="Bob", breed="persian", toy="string")
print(blue)
print(blue.species)

    # def __init__(self, name, species, breed, toy):
    #     self.name = name
    #     self.species = species
    #     self.breed = breed
    #     self.toy = toy

    # species
    # name
    # breed
    # favorite_toy


# blue = Cat("blue", "cat", "persian", "string")


# a = Animal()
# a.make_sound("MEEeooow")

# blue = Cat()
# blue.make_sound("Meoow")

# print(blue.cool)
# print(Animal.cool)

# Cat is a child of Animal
# blue is an instance of Cat

# print(isinstance(blue, Cat))
# print(isinstance(blue, Animal))
