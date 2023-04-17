#Write a Python program to calculate the area of a triangle given its base and height.

def calculate_triangle_area(base, height):
    area = (base * height) *0.5
    return area

input_base = float(input("Enter a base value: "))
input_height = float(input("Enter a height value: "))

result = calculate_triangle_area(input_base, input_height)
print("The area of triagnle is: ", result)
