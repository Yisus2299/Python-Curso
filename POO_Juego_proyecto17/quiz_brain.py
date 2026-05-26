class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.score = 0
        self.question_number = 0

    def still_has_questions(self):
        #esta es la forma mas dificil de hacerlo, pero podemos hacerlo de la siguiente manera:
        return self.question_number < len(self.question_list)
        #esta es la forma mas facil de hacerlo, pero podemos hacerlo de la siguiente manera:
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Acertaste!")
        else:
            print("Fallaste.")
        print(f"Tu respuesta correcta fue: {correct_answer}")
        print(f"Tu puntaje actual es {self.score}/{self.question_number}")
        print("\n")
            