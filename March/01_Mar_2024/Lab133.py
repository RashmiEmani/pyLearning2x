# Using multiple exceptions
# in this code, if ValueError has not found the eeror, then it will use Exception error

try:
    a = int(input("Enter the number only \n"))
except ValueError as v:
    print(v)
except Exception as e:
    print(e)
