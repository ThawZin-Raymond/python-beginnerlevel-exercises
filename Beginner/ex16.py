#Write a Python program to remove all vowels from a given string.

str = input("Enter a string value: ")

vowels = "aeiouAEIOU"
#''.join(...) is a method that joins the elements of a list (or any iterable) into a single string, using the specified string as a separator. In this case, an empty string '' is used as the separator, so the resulting elements of the list are concatenated without any separator.
result = ''.join([char for char in str if char not in vowels])

print("Removed all vowels froma given string: ", result)        