string1 = input("Enter the anagram1 \n")
string2 = input("Enter the anagram2 \n")

if(sorted(string1) == sorted(string2)):
    print("Entered value is anagram")
else:
    print("Entered value is not an anagram")