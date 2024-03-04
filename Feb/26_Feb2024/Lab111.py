class Password:

    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    #public functions and GET and SET - to call private variables

    def get_password(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid password")

    def set_password(self, password):
        if len(password) > 10:
            self.password = password
            print("Set to correct password", self.password)
        else:
            print("Not allowed, weak password")


pwd = Password("Hacker123")
print(pwd.public_var)

#print(pwd.__password) # not allowed

pwd.get_password(True)
#pwd.get_password(False)

pwd.set_password("rashmi123456")