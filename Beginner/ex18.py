#Write a Python program to find the common elements between two lists.

def find_common_elements(list1, list2):
    common_elements = [elements for elements in list1 if elements in list2]
    return common_elements

list1 = input("Enter a first lists: ")
list2 = input("Enter a second lists: ")


result_common_elements = find_common_elements(list1, list2)
print("Common elements between two list: ", result_common_elements)
