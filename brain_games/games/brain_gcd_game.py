from random import randint

TASK = "Find the greatest common divisor of given numbers."


def get_question():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    if num2 > num1:
        num1, num2 = num2, num1
    question, correct_answer = generate_question(num1, num2)

    return question, correct_answer


def generate_question(num1, num2):
    question = f"{num1} {num2}"
    while num2 != 0:
        num3 = num1 % num2
        num1, num2 = num2, num3

    return question, str(num1)
