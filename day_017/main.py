# from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from data_web import question_data

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    question = quiz.next_question()
    if quiz.is_the_end():
        quiz.is_the_end()

