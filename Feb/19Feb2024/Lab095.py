def anagram(str1, str2):
    if(sorted(str1) == sorted(str2)):
        print("Entered value is anagram")
    else:
        print("Entered value is not an anagram")

str1 = input("Enter the anagram1 \n")
str2 = input("Enter the anagram2 \n")
anagram(str1, str2)