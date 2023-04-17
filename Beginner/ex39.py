#Write a Python program to calculate the area of a trapezoid given its bases and height.

def area_trapezoid(base1,base2,height):
    area = (base1+base2)/2 * height
    return area

base1 = float(input("Enter the length of base 1: "))
base2 = float(input("Enter the length of base 2: "))
height = float(input("Enter the length of height: "))

area = area_trapezoid(base1,base2,height)
print("The area of trapezoid is: ", area)