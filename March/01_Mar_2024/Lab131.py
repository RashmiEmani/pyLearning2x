# try, except and finally
# multiple exceptions

try:
    num1 = int(input("Enter the number 1 \n"))
    num2 = int(input("Enter the number 2 \n"))
    result = num1 / num2
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Result {result}")
finally:
    print("I will be executed anyhow!")

# We have multiple errors in above code
# if user enter the string input -> ValueError: invalid literal
# ZeroDivisionError: division by zero

a = int(input("Enter the num1 \n"))
# by experience you identify there is ValueError -> Good coding -> means if you know the exception
# if not will use Exception error -> it is bad coding practice