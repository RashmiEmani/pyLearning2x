# Herarchical Inheritance -> 1 father 2 or more child

class Father:

    def home(self):
        return "This is a Father"

class Rashmi(Father):
    #def home(self):
        #return "This is Rashmi's home"
    pass

class SisterRashmi(Father):

    def home(self):
        return "This is Sister's home"

rashmi = Rashmi()
print(rashmi.home()) #it call's rashmi func instead of father func bcz in python we have local func high pirority.
                       # if rashmi method is not having then it will call father method