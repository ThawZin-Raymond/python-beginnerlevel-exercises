#Write a Python program to check if a given string is a palindrome

user_input = input("Please enter string attribute value: ")

reversed_input = user_input[::-1]

if user_input == reversed_input:
    print("Given string is a palindrome.")
else:
    print("Given string is not a palindrome.")