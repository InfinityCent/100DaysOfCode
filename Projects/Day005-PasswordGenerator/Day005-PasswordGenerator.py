import string
import random

letters = list(string.ascii_letters)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '%', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
l = int(input("How many letters would you like in your password? "))
s = int(input("How many symbols would you like? "))
n = int(input("How many numbers would you like? "))

random_letters = []
for i in range(0, l):
    random_letters.append(random.choice(letters))

random_symbols = []
for i in range(0, s):
    random_symbols.append(random.choice(symbols))

random_numbers = []
for i in range(0, n):
    random_numbers.append(str(random.choice(numbers)))

combined_list = random_letters + random_numbers + random_symbols
random.shuffle(combined_list)

password = ''.join(combined_list)

print(f'Here is your password: {password}')
