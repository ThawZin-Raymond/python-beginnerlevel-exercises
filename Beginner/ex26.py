#Write a Python program to count the number of occurrences of an element in a list.

input_list = input("Please enter a list of numbers: ").split()

input_number = input("Please enter a number to find in a list: ")

count = input_list.count(input_number)

print("THe number of occurance of ", input_number,"in a list is: ", count)