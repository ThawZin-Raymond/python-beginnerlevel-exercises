#Write a Python program to find the sum of all elements in a list.

input_list = input("Enter a list of number by spacing between them: ").split()

numbers = list(map(int,input_list))

sum_of_numbers = sum(numbers)

print("The sum of all numbers in a list: ", sum_of_numbers)