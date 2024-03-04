#Public , Protected and Private variables
class Car:
    name = None
    password = "123"
    # to hide the password -> introduced 3 types of data members or class variables

    def __init__(self, name): #__private constructor of this class
        self.public_var = "public" # Public var -> anyone can access
        self._protected_var = "protected123" # Protected
        self.__private_var = "pass@123"  # Private
        self.__password = "123"

    def _protected_method(self):
        print("Protected!")

    def __private_method(self):
        print("I am allowed to use the private variable because iam in the class" + self.__password)

    def printName(self):
        print(self.name)


#xuv = Car("XUV")
xuv = Car()
#xuv.printName()

print(xuv.public_var)
print(xuv._protected_var)
xuv._protected_method()
#print(xuv.__init__) # we cannot call this because it is private in nature or function
#print(xuv._password) #_protected variable call
#print(xuv.__password) #__private variable call, we have to define a function
print(xuv.__private_var) # not allowed to call directly, you can encapsulate private func as public func,
                         # then it is possible to call private data. for more, check for next example(Lab108)
#xuv.__private_method() # not allowed