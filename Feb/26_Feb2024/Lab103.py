class Car:
    name = None
    make = None
    model = None

    def __init__(self): # non - parameterised constructor, in python it is not used
        print("Hi , i will be called when a object is created")

    def __init__(self, obj_name, obj_make, obj_model): #special func, automatically called when obj is created. init is constructor
        self.name = obj_name
        self.make = obj_make
        self.model = obj_model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)

obj_lambo = Car("Lambo", "V2", "2024")
obj_lambo.start_engine()

print("------")

obj_xuv = Car("XUV", "V6", "2023")
obj_xuv.start_engine()

#obj_alto = Car()
#obj_alto.start_engine() #non - parameterised constructor, in python it is not used