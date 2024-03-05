class MyCustomException(Exception):
    def __init__(self, message):
        self.message = "message"
        super().__init__(message)


balance = 100
withdraw_amount = int(input("Enter the amount you can withdraw \n"))

if withdraw_amount > balance:
    raise MyCustomException("Balance is low")
else:
    print("Total amount after withdraw", balance - withdraw_amount)