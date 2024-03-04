# Take two numbers from the user and we want to add them

# step1 = Take input
# step2 = add or sum

num1 = input("Enter the first number")
num2 = input("Enter the second number")
# another way to convert str -> int
#num1 = int((input("Enter the first number"))
#num2 = int(input("Enter the second number"))
print(num1)
print(num2)
print(type(num1))
# num3 = num1 + num2 # it takes as string because str -> str -> contact (combine them or join them)
num3 = int(num1) + int(num2) # data type int is used to covert str to int
# str -> int -> int()
# int -> str -> str()
print(num3)
print(type(num3)) # shows date type of number