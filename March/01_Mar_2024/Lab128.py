# Exceptions
# to handle errors
# An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. 

a = int(input("Enter the num1 \n"))
b = int(input("Enter the num2 \n"))

c = a / b # ZeroDivisionError: division by zero
print("Division is ", c)
print("This is important message that we need to show to user")

# Ex - ATM -> SBI
# 1. ATM -> Insert card -10k
# 2. After -> Enter pin - 0000
# 3. Money Deducted. Error - RED SCREEN
# Problem in code -> Developer -> he/she didn't handle the exception very well
# Bad user experience
# User will curse you
