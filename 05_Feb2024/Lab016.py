# length of string

name = "batman"
print(len(name))  # len start from 1
print(name[0])  # [] represents index value -> starts from 0-5
print(name[4])
print(name[5])
# print(name[6])  #IndexError: string out of range

print(len(name)-1)
print(name[len(name)-1])

# string -> Immutability (that can't be changed or modified)
string = "hello"
# string[0] = "R" # TypeError: 'str' object does not support item assignment
string = "Rashmi"
print(string)
# we can't the chnage the value but we can change to whole value string = "rashmi"