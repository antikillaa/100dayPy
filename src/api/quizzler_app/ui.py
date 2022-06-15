import time
from tkinter import Tk, Canvas, PhotoImage, Button, Label

from src.api.quizzler_app.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi(Tk):

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()
        self.quiz = quiz_brain
        self.title("Quizzler")
        self.score = quiz_brain.score
        self.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=250,
                                                     text="Some question",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, pady=10, padx=10,
                                   highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(column=1, row=2)

        true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_image, pady=10, padx=10,
                                  highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(column=0, row=2)
        self.get_next_question()

        self.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_t = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_t)
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="We reached the end of the test")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_answer_true(self):
        correct = self.quiz.check_answer(True)
        self.set_score(correct)

    def check_answer_false(self):
        correct = self.quiz.check_answer(False)
        self.set_score(correct)

    def set_score(self, correct):
        if correct:
            self.canvas.config(bg="Green")
            self.canvas.update()
            self.score += 1
        else:
            self.canvas.config(bg="Red")
            self.canvas.update()
        self.canvas.after(1000, self.get_next_question())

