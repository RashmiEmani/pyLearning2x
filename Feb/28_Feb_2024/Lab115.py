# Herarchical Inheritance -> 1 father 2 or more child

class Vehicle:

    def info(self):
        return "This is Vehicle"

class Car(Vehicle):
    def info(self):
        return "This is Car"
    #pass

class Bicycle(Vehicle):

    def info(self):
        return "This is Bicycle"

car = Car()
bicycle = Bicycle()

print(car.info()) # it call's car func instead of vehicle func bcz in python we have local func high pirority.
                       # if car method is not having then it will call vehicle method