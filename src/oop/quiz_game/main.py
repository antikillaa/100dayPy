from src.oop.quiz_game.data import question_data
from src.oop.quiz_game.question_model import Question
from src.oop.quiz_game.quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz \n Your final score is {quiz.score}")
