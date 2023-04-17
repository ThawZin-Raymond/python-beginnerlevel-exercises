#Write a Python program to check if a given year is a leap year.

year = int(input("Please enter any year to check if it is a leap year or not: "))

if year % 4 == 0:
    print("It is a leap year.")
elif year % 4 != 0:
    print("It is not a leap year")
else:
    print("Error: invalid input")
