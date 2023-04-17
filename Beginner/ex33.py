#Write a Python program to capitalize the first letter of each word in a given sentence.

def capitalize_first_letter(given_sentence):
    #split the sentence into words
    words = given_sentence.split()
    #capitalize the first letter of each word
    capitalize_words = [word.capitalize() for word in words]
    #Join the capitalized words back into a sentence
    capitalize_words = ' '.join(capitalize_words)

    return capitalize_words

given_sentence = input("Enter a sentence: ")

capitalize_sentence = capitalize_first_letter(given_sentence)
print("Capitalized sentence: ",capitalize_sentence)

