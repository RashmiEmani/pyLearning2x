# Encapsulation -> Data memebers / Class Variables / Functions - they are closed within a single blueprint
# Wrapping or binding the data variables with the methods
# Encapsulation -> bind the data var and methods(reason to bind because to hide the important variables. e.g. password)

class Car:
    name = None

    def __init__(self, name):
        self.name = name # Public var -> anyone can access

    def printName(self):
        print(self.name)


xuv = Car("XUV")
xuv.printName()

lambo = Car("lambo")
lambo.printName()

print(xuv.name)
print(lambo.name)