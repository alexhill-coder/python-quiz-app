# Retrieves the html module.
import html


class QuizBrain:

    # Stores all the relevant information needed for the app.
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # Checks to see if the number of questions from an array is less than the question number.
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Retrieves the current question, sets up the next question and returns the question in
    # a formatted string format.
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    # Checks to see if the user answered correctly and returns true or false.
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
