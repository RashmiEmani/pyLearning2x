class Person:
    #Class Variable / Instance Variable
    name = None
    name = "Amit" #if we declare the value here, it will overwrite same value to all persons, to overcome this, use consctructors
    age = None

    def walk(self):
        a = 10 #local variable
        print("Hi your name is", self.name)
        print("Hi your age is", self.age)
        print(a)

amit = Person()
amit.walk()

pramod = Person()
pramod.walk()