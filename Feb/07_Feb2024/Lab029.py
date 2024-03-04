#Ternary Operator
x = 10
y = 20
# will cover in loops

# String Concat
str1 = "Hello"
str2 = "World"
str3 = str1 + str2 # + is not  to concate something
print(str3)

name = "Rashmi"
age = 33
#r = name + age
r = name + str(age)
print(r) # TypeError: can only concatenate str (not "int") to str

g = "Hello"
g += "World"
g = g + "World"
print(g)

# Increment and Decrement Operator -> ++ and --
x = 5
x += 1
x -= 1
print(x)

x = 10
y = ++x # this is not possible in python
y = x + 1 # this is used in python