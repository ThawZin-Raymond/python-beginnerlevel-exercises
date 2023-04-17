#Write a Python program to find the average of elements in a list.

input_list = input("Enter a list of numbersby spacing betwenn each number: ").split()

numbers = list(map(float,input_list))

sum_of_numbers = sum(numbers)

average_numbers = sum(numbers) / len(numbers)

print("The average of all numbers in a list: ", average_numbers)