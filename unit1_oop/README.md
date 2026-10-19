# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.


---------------------------
# Implementation Documentation

## Parent Class

I created a parent class representing a fantasy RPG character. The class included a shared game variable and three instance variables for the character's name, health, and level. I also created a method to display the character's information

## Child Class and Inheritance

I created a Warrior child class that inherited from the parent class. I used super() to reuse the parent's constructor and display method. I added a weapon, weapon durability, and attack method to the child class.

## Class and Instance Namespaces

I created two warrior objects and demonstrated accessing a class variable through both the class and an object. I addded a unique title attribute to one Warrior and used __dict__ to display the class and instance namespaces

## Shallow and Deep Copying

I created a Warrior with an inventory that contained a nested list. I used copy() and deepcopy() to create shallow and deep copies. After adjusting the original inventory, the shallow copy reflected the change while the deep copy did not.

## Student Created Extenstion

I implemented an attack system that reduced weapon durability by 2% with each attack. I used max() to prevent durability from going below zero.

## Testing

I executed the program in PyCharm and verified that each class displayed their attributes. I also verified inheritance, namespace and copying worked as expected.

I tested an edge case by creating a Warrior with 1% weapon durability and attacking twice. The durability stopped at 0%, preventing it from going negative.

In a real world RPG, this type of durability system could be used to manage all equipment durability and prevent invalid (negative) values.