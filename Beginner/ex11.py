#Write a Python program to generate a random number between a given range.
import random

lower_num = int(input("Enter a lower number: "))
higher_num = int(input("Enter a higher number: "))

if lower_num > higher_num:
    print("Error: lower number should be lower than higher number")
else:
    random_num = random.randint(lower_num,higher_num)
    print("Random number between a given range is: ",random_num)