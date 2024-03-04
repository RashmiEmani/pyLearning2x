def check(string, sub_string):
    if(string.find(sub_string) == -1):
        print("No! it is  not present in the string")
    else:
        print("Yes! it is present in the string")

#string = "concatnate"
#sub_string = "cat"
string = input("Enter the string \n")
sub_string = input("Enter the sub_string \n")
check(string, sub_string)
