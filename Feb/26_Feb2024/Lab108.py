class MyClass:

    def __init__(self):
        self.name = "Amit" #public var

    def public_func(self):
        print("Public Function")

    def __private_func(self):
        print("Private Function")

    def public_func_private(self): # encapsulating or binding private func to public func because
                                                     # we can't call private datta or function directly
        self.__private_func()

# Security -> not everyone can access your variables, we use private variable or functions. ex. password

a = MyClass()
a.public_func()
# a.__private_func() # not allowed to call directly(part of class), you can encapsulate private func as public func,
                       # then it is possible to call private data
a.public_func_private()