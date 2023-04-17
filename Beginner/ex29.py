#Write a Python program to remove an element from a list by its value.

def remove_element(given_list,given_value):
    removed_element = given_list.remove(given_value)
    return removed_element

input_list = input("Enter a list of element by spacing between them: ").split()
input_value = int(input("Enter a value to remove from the lsit: "))


input_list = list(map(int,input_list))

if input_value in input_list:
    result = remove_element(input_list,input_value)
    print("The remove element is: ", input_value)
    print("After removing element, the result will be: ",input_list)
else:
    print("The element is not in the list.")
