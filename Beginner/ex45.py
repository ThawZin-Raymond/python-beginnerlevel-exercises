#Write a Python program to calculate the area of a pyramid given its base area and height
import math

def calculate_pyramid_area(length, width, height):
    area = (length * width) + length * math.sqrt((width * 0.5) ** 2 + height ** 2) + width * math.sqrt((length * 0.5) ** 2 + height ** 2 )
    return area

input_length = float(input("Enter a value of length: "))
input_width = float(input("Enter a value of width: "))
input_height = float(input("Enter a value of height: "))

result = calculate_pyramid_area(input_length, input_width, input_height)

print("The area of pyramid is: ", result)