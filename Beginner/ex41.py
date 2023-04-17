#Write a Python program to calculate the area of a cube given its side length.

def calcualte_cube_area(length):
    area = 6 * (length ** 2)
    return area

input_length = float(input("Enter a length of cube: "))
result = calcualte_cube_area(input_length)

print("Area of cube is: ", result)