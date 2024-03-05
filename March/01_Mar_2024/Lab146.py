with open("td.txt", "r") as file:
    lines = file.readlines()

print(lines) #prints lines in list format
for line in lines: # line by line
    print(line, end="") #end for single line

with open("td.txt", "a") as file: #append means to add new line
    file.write("\ncharan")