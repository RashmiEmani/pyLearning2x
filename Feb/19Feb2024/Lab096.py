string = input("Enter the value \n")
string1 = string.lower()
vowels = 0
constants = 0

for i in string1:
    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        vowels = vowels + 1
    else:
        constants = constants + 1
print("vowels")
print(vowels)
print("constants")
print(constants)