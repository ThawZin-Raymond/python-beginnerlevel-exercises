#Write a Python program to count the occurrence of a given character in a string.

str = input("Enter a string value: ")
char_to_count = input("Enter a character to count: ")

count = str.count(char_to_count)

print("Count of ", char_to_count, "in the string: ", count)


