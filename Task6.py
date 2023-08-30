import math

class Shape:
    def calculate_area(self, *args):
        print("No shapes is matched")
        return 0

class Square(Shape):
    def calculate_area(self, *args):
        if 'side_length' in args:
            side_length = float(input("enter side_length value of square"))
            return side_length ** 2
        else:
            return super().calculate_area(*args)

class Triangle(Square):
    def calculate_area(self, *args):
        if 'base' in args[0] and 'height' in args[0]:
            base = float(input("enter base value of  Triangle"))
            height = float(input("enter height value of  Triangle"))
            return 0.5 * base * height
        else:
            return super().calculate_area(*args)

class Circle(Triangle):
    def calculate_area(self, *args):
        if 'radius' in args:
            radius=float(input("enter a radius value"))

            return math.pi * (radius ** 2)
        else:
            return super().calculate_area(*args)

#create object for Class Circle ,because it has all methods inheritence from each class
circle = Circle()


# Calculate areas using the same method name in each class

shape=input("enter shape for calculating area")

d={"square":"side_length","circle":"radius","triangle":["base","height"]}

area = circle.calculate_area(d[shape])

print(f"{shape} of the circle: {area}")

