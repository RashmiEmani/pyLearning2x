# To Handle Exception -> Use try and except block
# try -> try the code
# except -> execute the except code, if there is problem in try

a = int(input("Enter the num1 \n"))
b = int(input("Enter the num2 \n"))

try:
    c = a / b # ZeroDivisionError: division by zero
    print("Division is ", c)
except Exception as e: # no red line error if we use try and except block
    print(e)
    print("Zero Division, Please don't use B as zero!")

print("This is important message that we need to show to user")
