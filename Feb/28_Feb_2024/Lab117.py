# Multiple Inheritance -> 2 Parents 1 Child

# F, M -> S

class Father:

    def father_money(self):
        return "5"

    def home(self):
        return "This is from Father"

class Mother:


    def mother_money(self):
        return "2"

    def home(self):
        return "This is from Mother"

class Son(Father, Mother): # Multiple Inheritance -> In java we cannot have multiple inheritance, but in python it is possible
    def home(self):
        return "This is from Son"

        #pass

son = Son()
print(son.father_money())
print(son.mother_money())
print(son.home()) # it calls first priority given in son's class
# MRO -> Method Resolution Order
#print(Son.mro()) # shows order of which will be called first
