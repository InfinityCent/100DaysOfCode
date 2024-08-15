import random

print('''                                                                                              
,   .          |                  ,---.                    o              ,---.               
|\  |.   .,-.-.|---.,---.,---.    |  _..   .,---.,---.,---..,---.,---.    |  _.,---.,-.-.,---.
| \ ||   || | ||   ||---'|        |   ||   ||---'`---.`---.||   ||   |    |   |,---|| | ||---'
`  `'`---'` ' '`---'`---'`        `---'`---'`---'`---'`---'``   '`---|    `---'`---^` ' '`---'
                                                                 `---'                        ''')
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

def run_game():
    # Set game difficulty
    difficulty = input("Choose a difficulty. Easy/Hard: ").upper()
    while not difficulty in ["EASY", "HARD"]:
        difficulty = input("Invalid difficulty. Type Easy or Hard: ").upper()

    if difficulty == "EASY":
        ATTEMPTS = 10
    elif difficulty == "HARD":
        ATTEMPTS = 5


    # Get a random number
    RANDOM_NUMBER = random.randint(1, 100)


    attempts_left = ATTEMPTS
    user_guess = int(input(f"Guess a number. You have {attempts_left} attempts remaining: "))
    while (user_guess != RANDOM_NUMBER) and (attempts_left > 1):
        attempts_left -= 1
        attempts_plural = "attempts"
        if attempts_left == 1:
            attempts_plural = "attempt"
        if user_guess > RANDOM_NUMBER:
            user_guess = int(input(f"Too high. You have {attempts_left} {attempts_plural} remaining: "))
        else:
            user_guess = int(input(f"Too low. You have {attempts_left} {attempts_plural} remaining: "))

    if user_guess != RANDOM_NUMBER:
        replay = input(f"Sorry, you lost! The number was {RANDOM_NUMBER}. Do you want to play again? Yes/No:").upper()
    else:
        replay = input("Congratulations! You guessed the correct number. Do you want to play again? Yes/No: ").upper()

    if replay == "YES":
        run_game()


run_game()
