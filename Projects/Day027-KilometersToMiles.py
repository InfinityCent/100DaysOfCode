from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Kilometers to Miles Converter")
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)

#Entries
entry = Entry(width=30)
entry.insert(END, string="")
entry.grid(row=0, column=1)

# Label
label1 = Label(text="Kilometers")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label(text="0")
#label3.config(text="This is new text")
label3.grid(row=1, column=1)

label1 = Label(text="Miles")
label1.grid(row=1, column=2)


#Buttons
def action():
    km = int(entry.get())
    miles = km / 1.609344
    label3.config(text=f"{round(miles, 2)}")


button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)





#Labels
#label = Label(text="This is old text")
#label.config(text="This is new text")
#label.pack()


window.mainloop()