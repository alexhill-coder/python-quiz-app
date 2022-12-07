# Uses the tkinter module and retrieves the class from the quiz_brian file.
from tkinter import *
from quiz_brain import QuizBrain

# Sets the color theme of the app.
THEME_COLOR = "#375362"


class QuizInterface:

    # Sets the window screen parameters.
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Sets the score text and position.
        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        # sets the question text format, position & question background.
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, text="Some question text", width=280,
                                                font=("Ariel", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #  Uses and sets an image for the true button.
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        # Uses and sets an image for the false button.
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        # Calls the function to retrieve the next question.
        self.get_next_question()

        self.window.mainloop()

    # If there are questions left it retrieves the next question and updates the score.
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)

        # If no questions are left it will display the final score and disable the buttons.
        else:
            self.canvas.itemconfig(self.question, text=f"Your final score was: "
                                                       f"{self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Checks to see if the user pressed the correct button.
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    # The background will briefly change its color green or red depending on
    # whether the answer was correct. After a delay will then retrieve the
    # next question or display the final score.
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
