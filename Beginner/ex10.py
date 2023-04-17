#Write a Python program to calculate and print the factorial of a given number.

num = int(input("Enter a number: "))

result = 1

if num < 0:
    print("Error: Factorial is not defined for negative numbers")
elif num == 0:
    print("The factorial number of zero is 1.")
else :
    for i in range(1,num + 1):
        result = result * i 
    print("The factorial result of given number is ", result)