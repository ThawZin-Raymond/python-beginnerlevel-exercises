#Write a Python program to find the length of the longest word in a list of words.

def find_longest_word(words):
    longest_word_len = 0
    for word in words:
        word_length = len(word)

        if word_length > longest_word_len:
            longest_word_len = word_length
    
    return longest_word_len 
input_list = input("Please enter a list of elements by using space between them: ").split()

longest_word_length = find_longest_word(input_list)

print("The longest word length in the list is: ", longest_word_length)