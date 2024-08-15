class QuizBrain:
    """
    Attributes:
        question_number
        questions_list
    """

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question_text = self.questions_list[self.question_number].text
        question_answer = self.questions_list[self.question_number].answer
        user_input = input(f"Q.{self.question_number + 1}: {question_text} (True/False)?: ")

        if user_input.lower() == question_answer:
            self.score += 1
            print("You got it right!")
            print(f"The correct answer was: {question_answer.capitalize()}")
            print(f"Your score is {self.score}/{self.question_number + 1}")

        else:
            print("You got it wrong!")
            print(f"The correct answer was: {question_answer.capitalize()}")
            print(f"Your score is {self.score}/{self.question_number + 1}.")

        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
