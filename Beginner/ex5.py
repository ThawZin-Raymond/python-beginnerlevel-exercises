#Write a Python program to swap the values of two variables without using a temporary variable.

var1 = float(input("Please enter the first variable: "))
var2 = float(input("Please enter the second variable: "))

print("We are going to swap the values of two variables.")
print("The value of first variable before swaping is ", var1)
print("The value of second variable before swaping is ", var2)

var1, var2 = var2, var1

print("The value of first variable after swaping is ", var1)
print("The value of second variable after swaping is ", var2)