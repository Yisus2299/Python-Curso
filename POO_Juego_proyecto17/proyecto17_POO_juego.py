from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"].lower()
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("\n")
print("Haz completado el quiz")
print(f"tu puntae final fue: {quiz.score}/{quiz.question_number}")