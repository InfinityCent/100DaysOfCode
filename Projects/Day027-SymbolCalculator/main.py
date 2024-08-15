from tkinter import *
from symbol_class import ArcaneSymbol

# Creating a new window and configurations
window = Tk()
window.title("MapleStory Arcane/SAC Symbol Calculator")
window.minsize(width=500, height=500)

# INITIATE CLASS ---------------------------------------------------------
# symbol = ArcaneSymbol("Vanishing Journey")
# ------------------------------------------------------------------------

# TITLE ------------------------------------------------------------------
# Labels
label0 = Label(text="Welcome to the Maplestory Symbol Calculator!")
label0.place(relx=0.5, rely=0.02, anchor="center")
# ------------------------------------------------------------------------

# QUESTION 1 ------------------------------------------------------------------
# Labels
label1 = Label(text="1. [REQUIRED] Please select a symbol below: ")
label1.place(relx=0.0, rely=0.1, anchor="w")


# Radiobutton
radio_state = StringVar()
radiobutton1 = Radiobutton(text="Vanishing Journey", value="Vanishing Journey", variable=radio_state,
                           tristatevalue="x")
radiobutton2 = Radiobutton(text="Chu Chu Island", value="Chu Chu Island", variable=radio_state,
                           tristatevalue="x")
radiobutton3 = Radiobutton(text="Lachelein", value="Lachelein", variable=radio_state,
                           tristatevalue="x")
radiobutton4 = Radiobutton(text="Arcana", value="Arcana", variable=radio_state,
                           tristatevalue="x")
radiobutton5 = Radiobutton(text="Morass", value="Morass", variable=radio_state,
                           tristatevalue="x")
radiobutton6 = Radiobutton(text="Esfera", value="Esfera", variable=radio_state,
                           tristatevalue="x")
radiobutton1.place(relx=0, rely=0.15, anchor="w")
radiobutton2.place(relx=0, rely=0.2, anchor="w")
radiobutton3.place(relx=0, rely=0.25, anchor="w")
radiobutton4.place(relx=0, rely=0.3, anchor="w")
radiobutton5.place(relx=0, rely=0.35, anchor="w")
radiobutton6.place(relx=0, rely=0.4, anchor="w")

# ------------------------------------------------------------------------

# QUESTION 2 ------------------------------------------------------------------
# Labels
label2 = Label(text="2. [OPTIONAL] What is your symbol's level and how many "
                    "symbols have you equipped so \nfar in this level?", justify="left")
label2.place(relx=0, rely=0.5, anchor="w")

label21 = Label(text="Symbol level: ")
# label.pack(side="left")
label21.place(relx=0, rely=0.56, anchor="w")


# Spinbox
spinbox = Spinbox(from_=1, to=20, width=5)
spinbox.place(relx=0.16, rely=0.56, anchor="w")

label22 = Label(text="Symbols equipped in level: ")
label22.place(relx=0, rely=0.61, anchor="w")


# Entries
entry_var2 = StringVar()
entry2 = Entry(width=30, textvariable=entry_var2, validate="focusout")
entry2.insert(END, string="1")
entry2.place(relx=0.3, rely=0.61, anchor="w")
# -----------------------------------------------------------------------------

# QUESTION 3 ------------------------------------------------------------------
label3 = Label(text="3. [OPTIONAL] How many symbols do you earn per day?")
label3.place(relx=0, rely=0.71, anchor="w")


entry_var3 = StringVar()
entry3 = Entry(width=30, textvariable=entry_var3, validate="focusout")
entry3.insert(END, string="-1")
entry3.place(relx=0.01, rely=0.76, anchor="w")

# -----------------------------------------------------------------------------


# OUTCOME ------------------------------------------------------------------
# Buttons
def action():
    symbol_type = radio_state.get()
    curr_level = int(spinbox.get())
    curr_symbols = int(entry2.get())
    symbols_per_day = int(entry3.get())

    symbol = ArcaneSymbol(symbol_type=symbol_type, curr_level=curr_level,
                          curr_symbols=curr_symbols)
    if not symbols_per_day == -1:
        symbol.symbols_per_day = symbols_per_day

    time_remaining = symbol.symbol_needs()[2]
    mesos_needed = int(symbol.symbol_needs()[1])

    label_days = Label(text=f"Days to maxing out symbol: {time_remaining}")
    label_mesos = Label(text=f"Cumulative mesos needed: {mesos_needed:,}")

    label_days.place(relx=0.5, rely=0.91, anchor="center")
    label_mesos.place(relx=0.5, rely=0.96, anchor="center")


# calls action() when pressed
button = Button(text="Calculate!", command=action)
button.place(relx=0.45, rely=0.86, anchor="w")

window.mainloop()
