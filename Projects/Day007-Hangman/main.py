from typing import List
import random
from PyDictionary import PyDictionary

import random
from PyDictionary import PyDictionary


def load_words(words_path):
    """
    :return: List[str] of English words
    """
    with open(words_path, "r") as words:
        return list(words.read().split())


def get_random_word(words_list):
    """
    :words_list (List[str]): list containing English words

    :return: random word from list
    """
    return random.choice(words_list)


def get_word_definition(word):
    """
    :word (str): word to be guessed

    :return: print out each definition as a numbered list
    """
    word_definition = PyDictionary().meaning(word)
    word_definition = word_definition.values()

    for i in enumerate(word_definition):
        print(f'({i[0] + 1}) {i[1]}')


def evaluate_guess(word, guess, guess_list, hangmen_list):
    """
    :word (str): word to be guessed
    :guess (str): letter guessed by player
    :guess_list (List[str]): list containing _s and player guesses at
                             appropriate positions
    :hangmen_list (List[str]: list containing hangman text art

    :return: print the letters that have been guessed correctly at proper
             positions. If incorrect guesses, print _s as well as hangman
             text art.
    """
    # determine index of correct guess, mutate guess_list to reflect change
    # (turn _ to correct letter at appropriate position)
    if guess in word:
        for i in enumerate(word):
            if i[1] == guess:
                guess_list[i[0]] = guess

    # if guess incorrect, take away a life
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(hangmen_list.pop())
        print(f"You have {len(hangmen_list)} lives remaining.")

    print(' '.join(guess_list))


# load words here so it doesn't need to keep getting reloaded everytime game
# restarts
words_list = load_words("C:\\Users\\peree\\OneDrive\\Documents\\csc148-AlexDesktop\\assignments\\a2\\words.txt")


def run_hangman():
    print(''' _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                       ''')

    hangmen = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

    hangmen.reverse()  # reverse so it goes from alive to dead

    # choose random word from list
    random_word = get_random_word(words_list)
    guesses = ['_'] * len(random_word)

    get_word_definition(random_word)
    print(' '.join(guesses))

    while len(hangmen) > 0:  # while lives still remaining...
        if '_' not in guesses:  # word has been fully guessed
            print("You win! The man survived!")
            break

        else:
            # continue prompting player to make a guess
            player_guess = input("Guess a letter: ").lower()
            evaluate_guess(random_word, player_guess, guesses, hangmen)

    if len(hangmen) == 0:  # no lives remaining
        print(f"You failed. The correct word was {random_word}.")

    replay = input("Do you want to play again? Y/N").lower()

    if replay == 'y':
        run_hangman()


run_hangman()
