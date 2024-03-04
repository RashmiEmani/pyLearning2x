n = 7
num1 = 0
num2 = 1
num3 = num2
count = 1
while count <= n:
    print(num3)
    count += 1
    num1, num2 = num2, num3
    num3 = num1 + num2
    print()