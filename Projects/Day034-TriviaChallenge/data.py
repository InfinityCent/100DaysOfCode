import requests
NUM_QUESTIONS = 10
QUESTION_TYPE = "boolean"

parameters = {"amount": NUM_QUESTIONS,
              "type": QUESTION_TYPE}
request_questions = requests.get(url="https://opentdb.com/api.php", params=parameters)
request_questions.raise_for_status()
question_data = request_questions.json()["results"]
