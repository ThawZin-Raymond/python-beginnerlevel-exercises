#Write a Python program to calculate the power of a number.

def power_number(input_number):
    power_of_number= input_number ** 2
    return power_of_number

input_number = float(input("Enter a number to calculate the power of a number: "))
result = power_number(input_number)
print("The power of a number is ", result)

