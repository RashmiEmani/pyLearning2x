str = input("Enter the palindrome \n")

if(str == str[::-1]):
    print("Entered value is Palindrome")

else:
    print("Entered value is not a Palindrome")

print(str[::-1])