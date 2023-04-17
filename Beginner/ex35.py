#Write a Python program to check if a given sentence is a pangram.

def is_pangram(given_sentence):
    
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    given_sentence = given_sentence.lower()

    for char in alphabets:
        if char not in given_sentence:
            return False
        
    return True

given_sentence = input("Enter a sentence: ")

if is_pangram(given_sentence):
    print("The given sentence is a pangram.")
else:
    print("The given sentence is not pangram.")