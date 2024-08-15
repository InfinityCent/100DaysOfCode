import random


def random_cards(deck: list, num_cards: int) -> list:
    """

    :param deck: list of all cards that can be dealt
    :return: a list of two objects, with each object either being a number
             between 1-10 or an A, J, Q, or K
    """
    cards = []
    while len(cards) < num_cards:
        card = random.choice(deck)
        cards.append(card)
        deck.remove(card)

    return cards


def add_cards(hand: list) -> int:
    """

    :param hand: list containing numeric cards or A/J/Q/K
    :return: total value of cards added together
    """
    # all numerical cards are at face value
    # Joker, Queen, and King are 10
    # Ace is 11 if total doesn't go over 21; otherwise it's 1

    aces = ['A'] * hand.count('A')
    sum = 0
    for card in hand:
        if card in list(range(2, 11)):
            sum += int(card)
        elif card in ['J', 'Q', 'K']:
            sum += 10
        else:
            pass

    for ace in aces:
        if sum + 11 > 21:
            sum += 1
        else:
            sum += 11

    return sum


def won_or_lost(sum_cards: int) -> bool:
    """

    :param sum_cards: integer sum of all cards in hand
    :return: return True iff player has won or lost
    """
    if sum_cards == 21:
        print("Blackjack! You win!")
    elif sum_cards > 21:
        print("You lose!")
    else:
        pass


def run_blackjack():
    print("""
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """)

    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4

    user_hand = random_cards(cards, 2)
    computer_hand = random_cards(cards, 2)

    print(f"Your cards: {user_hand} = {add_cards(user_hand)}")
    print(f"Dealer's first card: [{computer_hand[0]}, HIDDEN] = {add_cards([computer_hand[0]])} + ?")
    print("\n")

    if add_cards(user_hand) == 21:
        print("Blackjack! You win!")
        return

    while add_cards(user_hand) < 21:
        action = input("Do you choose to STAND or HIT? Type 'stand' or 'hit': ")
        while (not action.isalpha()) or (action.lower() not in ['stand', 'hit']):
            action = input("Please only type 'stand' or 'hit'.")

        if action == 'hit':
            user_hand.append(random_cards(cards, 1)[0])
            print(f"Now your hand is: {user_hand} = {add_cards(user_hand)}")

        else:
            break

    if add_cards(user_hand) > 21:
        print("You lose!")
        return

    print(f"The Dealer's hand is: {computer_hand} = {add_cards(computer_hand)}")
    if add_cards(computer_hand) < 17:
        computer_hand.append(random_cards(cards, 1)[0])
        print(
            f"The Dealer drew another card. Now their hand is: {computer_hand} = {add_cards(computer_hand)}")
    print("\n")

    if add_cards(user_hand) > add_cards(computer_hand) or add_cards(computer_hand) > 21:
        print("You win!")
    elif add_cards(user_hand) < add_cards(computer_hand):
        print("You lose!")
    else:
        print("It's a draw!")


start = 'yes'
while start.lower() == 'yes':
    start = input(
        "Do you want to play a game of Blackjack? Type 'yes' or 'no'.")
    while (not start.isalpha()) or (start.lower() not in ['yes', 'no']):
        start = input("Please only type 'yes' or 'no'.")

    if start.lower() == 'yes':
        print("\n" * 200)
        run_blackjack()

