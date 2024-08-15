import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]

replay = "Y"
while replay == "Y":
    print("Welcome to Rock-Paper-Scissors!")
    user_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for "
                 "Scissors. "))
    if user_hand >= 3 or user_hand < 0:
        user_hand = random.randint(0, 2)
        print(f"Invalid number. Assigning a random hand: {hands[user_hand]}")

    else:
        print(hands[user_hand])

    computer_hand = random.randint(0, 2)

    print("Computer chose: ")

    print(hands[computer_hand])

    if user_hand == computer_hand:
        print("Draw.")

    elif (user_hand == 0 and computer_hand == 2) or \
            (user_hand == 1 and computer_hand == 0) or \
            (user_hand == 2 and computer_hand == 1):
        print("You win!")

    else:
        print("You lose!")

    replay = input("Play again? Y/N: ")
