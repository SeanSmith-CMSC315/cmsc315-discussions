"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # 1 class variable
    game = "Fantasy RPG"

    # At least 2 instance variables
    # Constructor (__init__)
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    # Display method
    def display_info(self):
        print(f"Name: {self.name}\n"
              f"Health: {self.health}\n"
              f"Level: {self.level}")



# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

# Uses inheritance
class ChildClass(ParentClass):
    # 1 new class variable
    character_type = "Warrior"

    # Override
    # 2 new instance variables (weapon & weapon_durability)
    def __init__(self, name, health, level, weapon, weapon_durability):
        super().__init__(name, health, level)
        self.weapon = weapon
        self.weapon_durability = weapon_durability

    # Override
    def display_info(self):
        super().display_info()
        print(f"Weapon: {self.weapon}\n"
              f"Weapon Durability: {self.weapon_durability}")

    # 1 new method
    def attack(self):
        self.weapon_durability = max(0, self.weapon_durability - 2)
        print(f"> {self.name} violently swings their {self.weapon}.\n"
              f"> Weapon Durability: {self.weapon_durability}%")

# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create 2 child objects
    warrior1 = ChildClass("Arthur", 100, 5, "Sword", 80)
    warrior2 = ChildClass("Julius", 200, 10, "Greatsword", 100)

    # Access variable through class
    # Access same variable through object
    print(f"ChildClass.character_type: {ChildClass.character_type}\n"
          f"warrior1.character_type: {warrior1.character_type}")

    # Add attribute to one object
    warrior1.title = "Champion"

    # Display both instance namespaces
    print("Warrior 1:", warrior1.__dict__)
    print("Warrior 2:", warrior2.__dict__)

    # Display class namespace
    print("Class:", list(ChildClass.__dict__.keys()))


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.


def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("\nTODO: Create and test your parent object")

    # An object that contains nested mutable data
    warrior = ChildClass("Arthur", 100, 5, "Sword", 80)
    warrior.inventory = ["Sword", ["Simple Meal"]]

    # Shallow copy shares nested mutable data
    shallow_warrior = copy(warrior)

    # Deep copy creates independent nested data (changes to the original don't affect the copy)
    deep_warrior = deepcopy(warrior)

    # Modify the original character's nested data
    warrior.inventory[1].append("Exquisite Meal")

    # Display original & copies
    print("Original:", warrior.inventory)
    print("Shallow Copy:", shallow_warrior.inventory)
    print("Deep Copy:", deep_warrior.inventory)

# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")
    character1 = ParentClass("Arthur", 100, 5)
    character1.display_info()

    print("\nTODO: Create and test your child object")
    character2 = ChildClass("Julius", 200, 10, "Greatsword", 100)
    character2.display_info()
    character2.attack()

    # Edge Case Test: Test weapon durability at extremely low levels
    print("\nEdge Case Test: Test weapon durability at extremely low levels")
    test_warrior = ChildClass("Test Warrior", 100, 1, "Dagger", 1)
    test_warrior.attack()
    test_warrior.attack()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()