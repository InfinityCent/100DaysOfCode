from tkinter import *
from tkinter import messagebox
from csv import writer
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- READ DATA ------------------------------ #
words_df = pandas.read_csv("data/german_words.csv",
                           encoding="ISO-8859-1",
                           low_memory=False)
known_words = pandas.read_csv("data/german_words_known.csv",
                              encoding="ISO-8859-1",
                              low_memory=False)

unknown_words = pandas.merge(words_df, known_words, indicator=True, how='outer') \
    .query('_merge=="left_only"') \
    .drop('_merge', axis=1)


def update_words(known_english="", known_german="", known_plural=""):
    global words_df, known_words, unknown_words

    if known_english != "" and known_german != "" and known_plural != "":
        # Open our existing CSV file in append mode
        # Create a file object for this file
        with open("data/german_words_known.csv", "a", newline="") as known_words_file:
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(known_words_file)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow([known_english, known_german, known_plural])

            known_words_file.close()

    known_words = pandas.read_csv("data/german_words_known.csv",
                                  encoding="ISO-8859-1",
                                  low_memory=False)

    unknown_words = pandas.merge(words_df, known_words, indicator=True, how='outer') \
        .query('_merge=="left_only"') \
        .drop('_merge', axis=1)


def get_random_word():
    global english, german, plural, gender

    random_row = unknown_words.sample(n=1)
    english = random_row.iloc[0, 0]
    german = random_row.iloc[0, 1]
    plural = random_row.iloc[0, 2]

    gender = "Undefined"
    if german.split()[0] == "Der":
        gender = "Masculine"
    elif german.split()[0] == "Die":
        gender = "Feminine"
    elif german.split()[0] == "Das":
        gender = "Neuter"

    return english, german, plural, gender


def empty_deck():
    global unknown_words

    if unknown_words.shape[0] == 0:
        messagebox.showinfo(title="German Flashcards",
                            message="You have correctly memorized all words! "
                                    "Your progress will be restarted.")

        with open("data/german_words_known.csv", "r+") as known_words_data:
            known_words_data.readline()  # read one line
            known_words_data.truncate(known_words_data.tell())  # terminate the file here

            known_words_data.close()

        update_words()
        next_word()


# -------------------------- FUNCTIONALITY ---------------------------- #
def flip_card():
    flip_back.grid(row=1, column=1)
    flip.grid_forget()

    global german, plural, gender

    if gender == "Masculine":
        canvas.itemconfig(canvas_image, image=card_masculine)
    elif gender == "Feminine":
        canvas.itemconfig(canvas_image, image=card_feminine)
    elif gender == "Neuter":
        canvas.itemconfig(canvas_image, image=card_neuter)

    canvas.itemconfig(canvas_text1, text=german, font=("Ariel", 40, "bold"))
    canvas.itemconfig(canvas_text2, text=plural, font=("Ariel", 40, "italic"))


def flip_back_card():
    flip_back.grid_forget()
    flip.grid(row=1, column=1)


    global english

    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(canvas_text1, text=english, font=("Ariel", 40, "bold"))
    canvas.itemconfig(canvas_text2, text="", font=("Ariel", 40, "italic"))


def next_word():
    global english, german, plural, gender, canvas
    english, german, plural, gender = get_random_word()

    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(canvas_text1, text=english)
    canvas.itemconfig(canvas_text2, text="")

    flip_back.grid_forget()
    flip.grid(row=1, column=1)


def correct_answer():
    global english, german, plural
    update_words(english, german, plural)

    try:
        next_word()
    except ValueError:
        empty_deck()


def incorrect_answer():
    next_word()


# ------------------------------ WORDS -------------------------------- #
# Starting word
try:
    english, german, plural, gender = get_random_word()
except ValueError:
    empty_deck()
# ---------------------------- UI SETUP ------------------------------- #
# UI
window = Tk()
window.title("German Flashcards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, highlightthickness=0)

# Images
card_front = PhotoImage(file="images/card_front.png")
card_masculine = PhotoImage(file="images/card_masculine.png")
card_feminine = PhotoImage(file="images/card_feminine.png")
card_neuter = PhotoImage(file="images/card_neuter.png")
right_button = PhotoImage(file="images/right.png")
wrong_button = PhotoImage(file="images/wrong.png")
flip_button = PhotoImage(file="images/flip.png")

canvas_image = canvas.create_image(400, 263, image=card_front)
canvas_text1 = canvas.create_text(400, 150, text=english, font=("Ariel", 40, "bold"))
canvas_text2 = canvas.create_text(400, 350, text="")
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=3)

# Buttons
right = Button(image=right_button, command=correct_answer, borderwidth=0, bg=BACKGROUND_COLOR)
wrong = Button(image=wrong_button, command=incorrect_answer, borderwidth=0, bg=BACKGROUND_COLOR)
flip = Button(image=flip_button, command=flip_card, borderwidth=0, bg=BACKGROUND_COLOR)
flip_back = Button(image=flip_button, command=flip_back_card, borderwidth=0, bg=BACKGROUND_COLOR)

right.grid(row=1, column=0)
wrong.grid(row=1, column=2)
flip.grid(row=1, column=1)
flip_back.grid_forget()

window.mainloop()
