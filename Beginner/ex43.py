#Write a Python program to calculate the area of a sphere given its radius.

import math

def calculate_sphere_area(radius):
    area = 4 * math.pi * radius * radius
    return area

input_radius = float(input("Enter a raidus value: "))

result = calculate_sphere_area(input_radius)

print("The area of sphere is: ",result)
