#Write a Python program to check if two given strings are anagrams.

def anagrams(str1,str2):
    str1 = str1.lower().replace(" ","")
    str2 = str2.lower().replace(" ","")

    sorted_str1 = sorted(str1) 
    sorted_str2 = sorted(str2) 

    if sorted_str1 == sorted_str2:
        print("Two given strings are anagrams.")
    else:
        print("Two given strings are not anagrams.")

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

anagrams(str1, str2)
