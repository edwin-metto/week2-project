import random


word_list = ["programming", "python", "coding", "javascript", "styling", "edwin"]


hangman_graphics = [
    '''
     -----
     |   |
         |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
         |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
     |   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|   |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    ''',
    '''
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    '''
]


def hangman():
    word = random.choice(word_list)
    word_length = len(word)
    guessed_word = ['_'] * word_length  
    guessed_letters = []  
    attempts_left = 6  

    print("Welcome to Hangman!")
    print(f"The word has {word_length} letters.")
    print("Let's start the game!")

    while attempts_left > 0:
        print(hangman_graphics[6 - attempts_left])
        print("\nCurrent word: ", " ".join(guessed_word))
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"You have {attempts_left} incorrect attempts left.")
        
        guess = input("Guess a letter: ").lower()

    
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Letter '{guess}' is not in the word.")
            attempts_left -= 1  

        if ''.join(guessed_word) == word:
            print(f"\nCongratulations! You guessed the word: {word}")
            break

    if attempts_left == 0:
        print(hangman_graphics[6]) 
        print(f"\nGame Over! The word was: {word}")
        print("You Lost.")


if __name__ == "__main__":
    hangman()
