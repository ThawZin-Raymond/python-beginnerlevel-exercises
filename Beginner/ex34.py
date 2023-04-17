#Write a Python program to count the number of words in a sentence.

def count_word(given_sentence):

    words = given_sentence.split()

    count_number = len(words)

    return count_number

given_sentence = input("Enter a sentence: ")

word_number = count_word(given_sentence)

print("The number of words in the list is: ",word_number)