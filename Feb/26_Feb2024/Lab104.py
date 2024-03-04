# Web Automation - Selenium

# Page - you are going automate

class VWOLoginPage:
    email = None
    password = None
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def loginconfirm(self):
      if self.password == "Pass123":
          print("You are allowed to enter")
      else:
          print("Invalid User")

obj_amit = VWOLoginPage("abc@abc.com","123")
obj_amit.loginconfirm()

obj_pramod = VWOLoginPage("bbb@abc.com","123")
obj_pramod.loginconfirm()

print(id(obj_amit))
print(id(obj_pramod))