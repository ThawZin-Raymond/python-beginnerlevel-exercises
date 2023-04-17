#Write a Python program to calculate and print the area of a rectangle given its length and width.
width = float(input("Please enter the value of width: "))
length = float(input("Pleease enter the value of length: "))

if width == 0 and length == 0:
    print("The values of width and length cannot be Zero.")
else:
    area = width * length
    print("The are of rectangle is: ", area)

