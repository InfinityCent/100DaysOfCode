from tkinter import *
from tkinter import messagebox
from pyperclip import copy
import string
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def search_website():
    website = website_box.get().lower()
    try:
        with open("saved_information.json", "r") as data_file:
            data = json.load(data_file)
            data_file.close()

    except FileNotFoundError:
        messagebox.showinfo(title="Password Manager",
                            message=f"You do not have any information saved "
                                    f"for {website_box.get()}.")
    try:
        saved_emailuser, saved_pass = data[website]['emailuser'], data[website]['password']
        messagebox.showinfo(title="Password Manager",
                            message=f"Saved information for {website_box.get()}:\n"
                                    f"Email/Username: {saved_emailuser}\n"
                                    f"Password: {saved_pass}")

    except KeyError:
        messagebox.showinfo(title="Password Manager",
                            message=f"You do not have any information saved "
                                    f"for {website_box.get()}.")


def generate_password():
    letters = list(string.ascii_letters)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list.extend(random.choice(letters) for _ in range(random.randint(8, 10)))
    password_list.extend(random.choice(numbers) for _ in range(random.randint(2, 4)))
    password_list.extend(random.choice(symbols) for _ in range(random.randint(2, 4)))

    random.shuffle(password_list)
    password = "".join(password_list)

    return password


def suggest_password():
    password = generate_password()
    pass_box.delete(0, END)
    pass_box.focus()
    pass_box.insert(0, password)

    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_box.get().lower()
    emailuser = emailuser_box.get()
    password = pass_box.get()
    data_dict = {
        website: {
            "emailuser": emailuser,
            "password": password
        }
    }

    not_empty = len(website) > 0 and len(emailuser) and len(password) > 0
    if not not_empty:
        messagebox.showinfo(title="Password Manager", message="Please fill all entries.")

    else:
        is_okay = \
            messagebox.askokcancel(title="Password Manager",
                                   message=f"Press OK to save the following "
                                           f"information:\nWebsite: "
                                           f"{website}\nEmail/Username: "
                                           f"{emailuser}\nPassword: "
                                           f"{password}")
        if is_okay:

            try:
                with open("saved_information.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("saved_information.json", "w") as data_file:
                    json.dump(data_dict, data_file, indent=4)
                    data_file.close()
            else:
                try:
                    saved_emailuser, saved_pass = data[website]['emailuser'], data[website]['password']
                except KeyError:
                    data.update(data_dict)
                    with open("saved_information.json", "w") as data_file:
                        json.dump(data, data_file, indent=4)
                        data_file.close()
                else:
                    update_info = \
                        messagebox.askokcancel(title="Password Manager",
                                               message=f"You already have information "
                                                       f"saved for {website_box.get()}:\n"
                                                       f"Email/Username: {saved_emailuser}\n"
                                                       f"Password: {saved_pass}\n\n"
                                                       f"Would you like to update your information?")
                    if update_info:
                        data[website]['emailuser'] = emailuser
                        data[website]['password'] = password
                        with open("saved_information.json", "w") as data_file:
                            json.dump(data, data_file, indent=4)
                            data_file.close()

            pass_box.delete(0, END)
            website_box.delete(0, END)
            website_box.focus()

            messagebox.showinfo(title="Password Manager", message="Information successfully saved.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website      ")
emailuser_label = Label(text="Email/Username      ")
pass_label = Label(text="Password      ")

website_label.grid(row=1, column=0)
emailuser_label.grid(row=2, column=0)
pass_label.grid(row=3, column=0)

# Textboxes
website_box = Entry(width=35)
emailuser_box = Entry(width=35)
pass_box = Entry(width=21)

website_box.grid(row=1, column=1, columnspan=2, sticky="ew")
emailuser_box.grid(row=2, column=1, columnspan=2, sticky="ew")
pass_box.grid(row=3, column=1, sticky="ew")

website_box.focus()
emailuser_box.insert(0, "common_email@gmail.com")

# Buttons
search = Button(text="Search", command=search_website)
generate_pass = Button(text="Generate Password", command=suggest_password)
add_button = Button(text="Add", width=36, command=save_info)

search.grid(row=1, column=3)
generate_pass.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
