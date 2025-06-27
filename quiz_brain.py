class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        cur_question = self.question_list[self.question_number]
        self.question_number += 1
        q_number = self.question_number
        u_answer = input(f"Q.{q_number}: {cur_question.text} (True/False): ")
        self.check_answer(u_answer, cur_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"Sorry, you got it wrong, the answer was {c_answer}")

        print(f"Your score is {self.score}/{self.question_number}.")
        print("\n")
