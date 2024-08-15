print("Welcome to the tip calculator.")
bill = float(input("How much was the total bill? $"))
percentageTip = 1 + (int(input("What percentage tip would you like to give? %"))
                     / 100)
numPeople = int(input("How many people are splitting this bill? "))

total = bill * percentageTip

print(f'Each person should pay ${round((total / numPeople), 2)}.')
