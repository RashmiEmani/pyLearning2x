# Polymorphism -> Object - Oriented Programming (oops)
# Ploy -> Many
# Morphism -> Form

# Object - Method -> Mother, Maternal she is, sister, parent - child (one person can have multiple roles)

# Poly has ->
# Method Over loading
# Method overriding

class Shape:

     def area(self):
         print("Area of shape")

class Rectangle(Shape):

     def __init__(self, length, width):
         self.length = length
         self.width = width

     def area(self):
         #print("Area of rectangle")
         return self.length * self.width

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # print("Area of circle")
        return 3.14 * self.radius * self.radius

shape1 = Rectangle(5,6)
print(shape1.area())

shape2 = Circle(20)
print(shape2.area())

shape3 = Shape()
shape3.area()