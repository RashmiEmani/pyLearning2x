# Abstraction -> Concept of OOPs
# Hiding the details and showing the what is required
# ex -> Do you know How engine is started?
# How gear box was managed?
# Hide the implementation and show only the important details
# 1. Abstract base classes
# 2. Abstract base methods

# Java -> Abstraction is done by Abstraction class and interface but we dont have this concept in python

from abc import ABC, abstractmethod #abc is inbuilt abstract class

class Animal(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod # it means it is incomplete method, we cant inherit the function
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        return "Bow Bow"

class Cat(Animal):

    def sound(self):
        return "Meow Meow"


#dog = Dog() # error -> Can't instantiate abstract class Dog without an implementation for abstract method 'sound'
             # you have to complete method in dog class
dog1 = Dog("Tony")
print(dog1.sound())
cat = Cat("Kitty")
print(cat.sound())
