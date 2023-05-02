print('What is the length of a side of the square?')
side = input('Please enter a number:')
side_string = float(side)
area = side_string ** 2
print(f'The area of the square is: {area}')
print()
print('What is the length a side of the rectangle?')
length = input('Please enter a number:')
print('What is the width of a side of the rectangle?')
width = input('Please enter a number:')
length_string = float(length)
width_string = float(width)
area = length_string * width_string
print(f'The area of the rectangle is: {area}')
print()
print('What is the radius of the circle?')
radius = input('Please enter a number:')
radius_string = float(radius)
area = (radius_string**2) * 3.14
print(f'The area of the circle is: {area}')
print()
# STRETCH 1: Using the math library
#IMPORT MATH
import math
radius = float(input('What is the radius of the circle?'))
area = math.pi * (radius ** 2)
print(f"The area of the circle is: {area}")
print()
print()
# STRETCH 2: Many areas from one value
value = float(input('What is the value to be used?'))
area_square =  value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4 / 3) * math.pi * (value ** 3)
print(f'Area of a square: {area_square}')
print(f"Area of a circle: {area_circle}")
print(f"Volume of a cube: {volume_cube}")
print(f"Volume of a sphere: {volume_sphere}")
print()
print()
# STRETCH 3: cm -> m conversion
side = float(input('What is the length of a side of the square (in cm)?'))
area = side ** 2
print(f"The area of the square is: {area} cm^2")
print()
print()
side = float(input('What is the length of a side of the square in cm^2 to m^2?'))
area = side ** 2
print(f"The area of the square is: {area / 10000} m^2")
print()
# AREA OF RECTANGLE
length = float(input("What is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"The area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")
print()
# AREA OF CIRCLE
radius = float(input("What is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"The area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")
print()
# AREA OF CUBE
length = float(input("What is the length of cube (in cm)? "))
width1 = float(input("What is the width of the cube (in cm)? "))
width2 = float(input("What is the width of the cube (in cm)? "))
area = length * width1 * width2
print(f"The area of the cube is: {area} cm^3")
print(f"The area of the cub is: {area / 1000000} m^3")