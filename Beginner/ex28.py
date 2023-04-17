#Write a Python program to concatenate two lists.

input_list1  = input("Please enter a first list of elements by using space between each element: ").split()
input_list2  = input("Please enter a second list of elements by using space between each element: ").split()

interger_list1 = list(map(int,input_list1))
interger_list2 = list(map(int,input_list2))

concatanate_list = input_list1 + input_list2
print(concatanate_list)