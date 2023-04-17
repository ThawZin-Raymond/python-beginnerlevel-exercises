#Write a Python program to find the second largest element in a list.

def find_secondLargest(input_list):

    if len(input_list) < 2:
        print("Error: List must be at least two elements.")
        return None
    
    input_list = list(map(float,input_list)) # Convert list of strings to list of floats
    sorted_list = sorted(set(input_list), reverse = True) #reverse = True sorts a list in descending order.
    print(sorted_list)

    if len(sorted_list) < 2:
        print("Error: List must be at least two unique elements.")
        return None
    
    second_largest = sorted_list[1]
    return second_largest

input_list = input("Enter a list of elements by spacing between them: ").split()
finalized_result = find_secondLargest(input_list)
print("Second largest elements in the list is: ", finalized_result)