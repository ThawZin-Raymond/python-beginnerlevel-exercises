#Write a Python program to sort a list in ascending order.

def ascending_order(input_list):
    if len(input_list) < 2:
        print("Error: The input list must have at least two elements.")
        return None
    
    input_list = list(map(float,input_list))
    sorted_list = sorted(set(input_list))

    if len(sorted_list) < 2:
        print("Error: The sorted list must have at least two elements.")
        return None
    
    return sorted_list

input_list = input("Enter a list of elements: ").split()
final_result = ascending_order(input_list)
print("The ascending order of given list: ", final_result)
    