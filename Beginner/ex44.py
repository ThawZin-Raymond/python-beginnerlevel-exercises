#Write a Python program to calculate the area of a cone given its radius and height.

import math

def calculate_cone_area(radius, height):
    area = math.pi * radius * (radius + math.sqrt( height ** 2 + radius ** 2))
    return area

input_radius = float(input("Enter a value of radius: "))
input_height = float(input("Enter a value of height: "))
result = calculate_cone_area(input_radius, input_height)
print("The area of cone is: ",result)