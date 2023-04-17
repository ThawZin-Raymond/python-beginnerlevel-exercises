#Write a Python program to find the index of a given element in a list.

input_list = input("Please enter a number of elements by separating space between them: ").split()

index_element = input("Please enter an element to find in the list: ")

try:
    index = input_list.index(index_element)
    print("The element ", index_element, "is at index ", index)

except ValueError:
    print("THe element ", index_element, "is not found in the list.")