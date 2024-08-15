class Question:
    """Attributions:
        text: str
        answer: str
    """

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer.lower()

    def evaluate(self, user_ans):
        return user_ans.lower() == self.answer
