starting_letter = "C:/Users/peree/OneDrive/Documents/100DaysOfCode/Projects/Day24-MailMerge/Input/Letters/starting_letter.txt"
names_file = "C:/Users/peree/OneDrive/Documents/100DaysOfCode/Projects/Day24-MailMerge/Input/Names/invited_names.txt"
output_directory = "C:/Users/peree/OneDrive/Documents/100DaysOfCode/Projects/Day24-MailMerge/Output/ReadyToSend"
PLACEHOLDER = "[name]"

def personalize_letter(letter_path, name_path):
    with open(name_path, mode="r") as name:
        names = name.readlines()

    for name in names:
        name = name.strip()

        with open(letter_path, mode="r") as letter:
            letter_lines = letter.read()

        letter_lines = letter_lines.replace(PLACEHOLDER, name)

        personalized_letter = open(f"{output_directory}/{name}.txt", mode="w")
        personalized_letter.write(letter_lines)
        personalized_letter.close()


personalize_letter(starting_letter, names_file)