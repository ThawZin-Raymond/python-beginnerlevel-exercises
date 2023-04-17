#Write a Python program to find the second smallest element in a list.

def find_secondSmallet(input_list):
    if len(input_list) < 2:
        print("Erro: The list must be at least two elements.")
        return None
    
    input_list = list(map(float,input_list))
    sorted_list = sorted(set(input_list))
    print("Sorted list: ", sorted_list)

    if len(sorted_list) < 2:
        print("Error: The sorted list must have at least two elements.")
        return None
    
    secondSmallest = sorted_list[1]
    return secondSmallest

input_list = input("Enter a list of elements by spacing between them: ").split()
final_result = find_secondSmallet(input_list)
print("Second smallest element in the list: ", final_result)

