from question_model import Question
from data import question_data
from src.api.quizzler_app.quiz_brain import QuizBrain
from src.api.quizzler_app.ui import QuizUi

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizUi(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
