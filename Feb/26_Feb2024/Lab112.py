# Single Inheritance -> getting something from grand father and father

class Father:

    __private_villa = "GOA"
    gold = "5kg"
    def drive_car(self):
        print("Lambo")

    def threebhk_flat(self):
        print("3bhk Flat")

    def private_villa_access(self, is_my_son):
        print(self.__private_villa)

class Son(Father): #Single Inheritance -> whatever father has son will get it. subclass 
    pass

pramod = Son()
print(pramod.gold)
pramod.drive_car()
pramod.threebhk_flat()
#print(pramod.__private_villa) #can't access private var

pramod.private_villa_access(True)

mmk = Father()
print(mmk.gold)
mmk.drive_car()
mmk.threebhk_flat()
#print(mmk.__private_villa) #can't access private var

