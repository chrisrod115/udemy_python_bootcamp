"""This Class will keep track of how well you are doing.
"""


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list


    def next_question(self):
        current_quesiton = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_quesiton.text} (True/False): ")