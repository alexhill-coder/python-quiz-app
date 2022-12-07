# Retrieves the classes and data from the other files.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# A list to store the questions.
question_bank = []

# Each of the retrieved questions are formatted and placed in the list.
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Checks the number of questions, whether the answer is true or false and
# returns the next questions string.
quiz = QuizBrain(question_bank)

# Controls the UI and updates to the users actions.
quiz_ui = QuizInterface(quiz)

# Will return the messages to the console once the program is closed.
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
