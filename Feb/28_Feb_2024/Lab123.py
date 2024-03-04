# Method Over loading
# Python does not support method overriding in the traditional sense
# Same name of a func with diff parameter

class MathUtil:

    def add(self, a, b=0, c=0):
        print(a+b+c)

    #def add(self, a, b, c): # python does not support method overriding
        #pass


math = MathUtil()
op1 = math.add(2) # b & c intial values passed
op2 = math.add(2,3)
op3 = math.add(2,3,5)