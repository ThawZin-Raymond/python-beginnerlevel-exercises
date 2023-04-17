#Write a Python program to calculate and print the area of a circle given its radius.
import math
radius = float(input("Please enter the value of radius: "))

if radius == 0:
    print("Error: the value of radius cannot be zero.")
else:
    area = math.pi * (radius ** 2)
    print("The area of circle is: ", area)