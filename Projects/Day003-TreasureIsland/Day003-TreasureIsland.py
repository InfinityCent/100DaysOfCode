print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

direction = input("You're at a crossroad. Do you want to go right or left? R/L: ")
while not (direction == 'R' or direction == 'L'):
    direction = input("You're at a crossroad. Do you want to go right or left? R/L: ")


if direction == 'R':
    print("Oops, you walked into a trap and died!")

elif direction == 'L':
    action = input("You come to a lake with an island in the middle. Type 'W' "
                   "to wait for a boat or type 'S' to swim across.")
    while not (action == 'W' or action == 'S'):
        action = input("You come to a lake with an island in the middle. Type "
                       "'W' to wait for a boat or type 'S' to swim across.")
    if action == 'S':
        print("Uh oh, you get gobbled up by a shark and die!")

    elif action == 'W':
        door = input("You arrive at the island unharmed. There is a house "
                     "with 3 doors; red, yellow, and blue. Which colour "
                     "do you choose? R/Y/B: ")
        while not (door == 'R' or door == 'Y' or door == 'B'):
            door = input("You arrive at the island unharmed. There is a house "
                         "with 3 doors; red, yellow, and blue. Which colour "
                         "do you choose? R/Y/B: ")

        if door == 'R' or door == 'B':
            print("The big bad witch opened the door and killed you!")

        elif door == 'Y':
            print("You win! You found a stash of treasure.")
