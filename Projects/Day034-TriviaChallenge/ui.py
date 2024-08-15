from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="",
                                                     width=280,
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.get_next_question()

        self.score_label = Label(text=f"Score: {self.quiz.score}",
                                 font=("Arial", 20, "normal"),
                                 fg="white",
                                 bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.evaluate_true)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.evaluate_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def change_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def evaluate_true(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.change_score()
        self.window.after(1000, self.get_next_question)

    def evaluate_false(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.change_score()
        self.window.after(1000, self.get_next_question)




