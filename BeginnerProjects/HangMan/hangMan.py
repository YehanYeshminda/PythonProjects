import random
# ? importing the needed files in order to run the words variable
from wordsFile import words

# ? import an alphabet string
import string


# ! Step 1 -  Get an random Word
random_word = random.choice(words)

def get_valid_word(listVal):
    random_word =  random.choice(listVal) # takes in an list and then chooses an list
    
    # ! step 2 get an valid random word
    while ' ' in random_word or '-' in random_word:
        random_word = random.choice(listVal)
    return random_word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # ! STEP 6 - convert the letters into -
        # ? if the letter is in the used letters show the used letter else show an - for each word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print(f"Current Lives {lives}")
        print('Current word: ', ' '.join(word_list))
        
        # ! STEP 1 - getting user input
        user_letter = input('Guess a letter: ').upper()
        
        # ! STEP 2 - If the user letter is in the alphabet and not in the used letters
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) 
            
            # ! STEP 3 - if the word is in the word letters which means an valid word
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            
            # ! STEP 3 - Remove an life if wrong
            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
                
        # ! STEP 4 - if the word is already guessed
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        # ! STEP 7 - if the word is not an valid string
        else:
            print('\nThat is not a valid letter.')

    # ! STEP 8 - If we run out of lives
    if lives == 0:
        print(f"Current Lives {lives}")
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
        
hangman()