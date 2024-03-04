# Method overriding
# child always override the parent function
# super means call to my parent
class Animal:

    def __init__(self):
        pass
    def sound(self):
        print("Animal Sound")

class Dog(Animal):

     def __init__(self):
         pass
     def sound(self):
         super().sound() #super is a keyword, calling data from animal
         print("Dog Sound")


animal = Animal()
animal.sound()

dog = Dog()
dog.sound()