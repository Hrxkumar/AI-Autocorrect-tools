import nltk
from nltk.corpus import words
nltk.download('words')

# create a set of valid English words
word_list = set(words.words())

# define a function to find the closest valid word
def find_closest_word(word):
    # if the word is already valid, return it
    if word in word_list:
        return word
    # otherwise, find the closest valid word
    else:
        # generate all possible corrections (add, remove, replace, or swap a letter)
        corrections = set()
        for i in range(len(word)):
            left, right = word[:i], word[i:]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                corrections.add(left + c + right)  # add a letter
                corrections.add(left + c + right[1:])  # remove a letter
                corrections.add(left + c + right[1:])  # replace a letter
                if len(right) > 1:
                    corrections.add(left + right[1] + c + right[2:])  # swap two letters
        
        # find the closest valid word from the corrections
        valid_corrections = word_list.intersection(corrections)
        if valid_corrections:
            return max(valid_corrections, key=word_list.index)
        else:
            return word  # if no valid corrections, return the original word

# take input from the user and correct it
while True:
    user_input = input('Enter a word to correct (or type "exit" to quit): ')
    if user_input == 'exit':
        break
    corrected_word = find_closest_word(user_input)
    print(f'Corrected word: {corrected_word}')
