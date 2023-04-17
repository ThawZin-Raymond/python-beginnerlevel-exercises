#Write a Python program to calculate the area of a cylinder given its radius and height.

import math

def calculate_cylinder_area(radius, height):
    area = (2 * math.pi * radius * height) + (2 * math.pi * radius * radius)
    return area

input_radius = float(input("Enter a value of radius: ")) 
input_height = float(input("Enter a value of height: "))

result = calculate_cylinder_area(input_radius,input_height)
print("The area of Cylinder is: ", result)