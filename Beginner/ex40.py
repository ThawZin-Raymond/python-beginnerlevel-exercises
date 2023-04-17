#Write a Python program to calculate the area of a parallelogram given its base and height.

def calculate_parallelogram_area(base,height):
    area = base * height
    return area

input_base = float(input("Enter a base value: "))
input_height = float(input("Enter a height value: "))

result = calculate_parallelogram_area(input_base,input_base)
print("The result of calculation for parallelogram area is: ", result)


