# Multi-level Inheritance -> 1 Gf, 1 Father and 1 Child

class GF:
    def home(self):
        print("5BHK")

class Father(GF):

    def home2(self):
        print("GOA")

class Son(Father):

    def home3(self):
        print("Hyd")

pramod = Son()
pramod.home()
pramod.home2()
pramod.home3()

f = Father()
f.home()
f.home2()
#f.home3() # can't access son's inheritance

gf = GF()
gf.home()
gf.home2() # can't access son's inheritance
gf.home3() # can't access son's inheritance