class GF:
    def car(self):
        return "Old Car"

class F(GF):
    def car(self):
        return "Hyndai I20"

class S(F):
    #def car(self):
        #return "Lambo"
    pass


son = S()
print(son.car())