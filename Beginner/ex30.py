#Write a Python program to remove an element from a list by its index.

def removed_index(input_list,remove_index):
    remove_element = input_list.pop(remove_index)
    return remove_element
input_list = input("Enter a list of numbers by using space between them: ").split()

remove_index = input("Enter an index value to remove the element in the list: ")

input_list = list(map(int,input_list))
remove_index = int(remove_index)

if remove_index < len(input_list):
    removed_element = removed_index(input_list,remove_index)
    print("Removed element: ",removed_element)
    print("After removing an element from a list by its index: ",input_list)

else :
    print("Index value must be less the length of the list.")
