#Write a Python program to find the square root of a given number.
import math

def squre_root(input_number):

    squre_root_result = math.sqrt(input_number)
    return squre_root_result

input_number = float(input("Enter a number to find the squre root of it: "))
result = squre_root(input_number)
print("The squre root of a given number is: ",result)

