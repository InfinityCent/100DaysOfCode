print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')

print("Welcome to the Secret Auction.")


def bidder_info() -> tuple[str, int, str]:
    """

    :return: a tuple with player name, their bid, and whether there's another bidder.
    """
    pn = input("What is your name? ")

    pb = input("What is your bid? $")
    while (not pb.isnumeric()) or (int(pb) < 0):
        pb = input("Please enter a positive numerical amount. $")

    ob = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    while ob not in ['yes', 'no']:
        ob = input("Please enter 'yes' or 'no' only: ").lower()

    return pn, int(pb), ob


bids = {}
other_bidders = 'yes'

while other_bidders == 'yes':
    player_name, player_bid, other_bidders = bidder_info()

    bids[player_name] = player_bid
    print('\n' * 200)


highest_bidder = max(bids, key=bids.get)
print(f'The winner is {highest_bidder} with a bid of ${bids[highest_bidder]}.')
