#Write a Python program to check if a given element is present in a list.

def check_element(input_list, check_number):
    if check_number in input_list:
        print("The given element, ",check_number, "is in the list.")
        return True
    else: 
        print("The given element, ",check_number, "is not in the list.")
        return False
    
input_list = input("Enter a list of elements: ").split()
input_list = list(map(int, input_list))
check_number = input("Enter an element which is present in the list: ")
check_number = int(check_number)

checked_number = check_element(input_list,check_number)


    