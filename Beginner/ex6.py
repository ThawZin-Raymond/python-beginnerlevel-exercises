#Write a Python program to check if a given number is even or odd.

number = input("Please enter a number to check if it is even or odd: ")

number = int(number) #convert input to interger

if number % 2 == 0:
    print("The given number ", number, " is even")
elif number % 2 != 0:
    print("The given number ", number, " is odd")
else:
    print("Error: invalid input")