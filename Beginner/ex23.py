#Write a Python program to sort a list in descending order.

def descending_order(input_list):

    if len(input_list) < 2:
        print("Error: The list must have at least two elements in it.")
        return None
    
    input_list = list(map(float,input_list))
    sorted_list = sorted(set(input_list),reverse = True)

    if len(sorted_list) < 2:
        print("Error: The sorted list must have at least two elements.")
        return None
    
    return sorted_list

input_list = input("Enter a list of elements by spacing between them: ").split()
final_result = descending_order(input_list)
print("The descending order of given list: ", final_result)