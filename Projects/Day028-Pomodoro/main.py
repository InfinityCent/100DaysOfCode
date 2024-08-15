from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="TIMER")
    label_checkmark.config(text="")
    global REPS
    REPS = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer(long_break_sec)
        label_timer.config(text="Long Break!", fg=RED)
    elif REPS % 2 == 0:
        timer(short_break_sec)
        label_timer.config(text="Short Break!", fg=PINK)
    else:
        timer(work_sec)
        label_timer.config(text="Work!", fg=GREEN)

    REPS += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def timer(time):
    timer_min = floor(time / 60)
    timer_sec = time % 60

    canvas.itemconfig(timer_text, text=f"{timer_min}:{timer_sec:02d}")
    if time > 0:
        global TIMER
        TIMER = window.after(1000, timer, time - 1)
    else:
        start_timer()
        label_checkmark.config(text=("✓" * floor(REPS/2)))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label_timer.grid(row=1, column=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

label_checkmark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
label_checkmark.grid(row=5, column=2)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=4, column=1)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=4, column=3)


window.mainloop()
