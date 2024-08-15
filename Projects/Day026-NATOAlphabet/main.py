import pandas

nato_abc = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_abc_dict = {
    row.letter: row.code for (_, row) in (nato_abc.iterrows())
}

user_word = "0"
while not user_word.isalpha():
    user_word = input("Please input a word to be deconstructed using the NATO alphabet: ").upper()
letters = list(user_word)
for letter in letters:
    print(f"{letter} as in {nato_abc_dict[letter]}")
