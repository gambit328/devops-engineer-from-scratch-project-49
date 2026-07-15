from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    num = randint(1, 20)
    correct_answer = "yes" if num % 2 == 0 else "no"
    return num, correct_answer
