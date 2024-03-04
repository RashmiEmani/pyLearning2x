# format string
# 2 x 1 = 2
num = 2

print(f"{num}*1 = {num}")
print(f"{num}*2 = {num*2}")
print(f"{num}*3 = {num*3}")

# . format method

b = 1
print("2*{}{}" .format(*args:b,2*b)) # typical method -> even we can't use in automation testing
print("{}{}{}" .format(*args:1,2,3))