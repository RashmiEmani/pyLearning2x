side1 = float(input("Enter the side1: "))
side2 = float(input("Enter the side2: "))
side3 = float(input("Enter the side3: "))

if(side1 == side2 == side3):
    print("Equilateral Traingle -> all sides are equal")
elif(side1 == side2 or side1 == side3 or side2 == side3):
    print("Isosceles Traingle -> exactly two sides are equal")
else:
    print("Scalene Traingle -> no sides are equal")
#elif(side1 != side2 and side1 != side3 and side2 != side3):
    #print("Scalene Traingle")