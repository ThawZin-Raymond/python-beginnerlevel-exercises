#Write a Python program to remove duplicates from a list.

def remove_duplicates(input_list):
    #convert list to set to remove duplicates automatically
    unique_set = set(input_list)

    #convert set to list
    unique_list = list(unique_set)

input_list = input("Please enter a list of elements: ").split()
print("Given list: ", input_list)
finalized_list = remove_duplicates(input_list)
print("Removed duplicates from a list: ", finalized_list)


