from random import randint


def get_questions():
    questions = []

    for _ in range(3):
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        if num2 > num1:
            num1, num2 = num2, num1
        questions.append(generate_question(num1, num2))

    return questions


def get_task():
    return "Find the greatest common divisor of given numbers."


def generate_question(num1, num2):
    question = f"{num1} {num2}"
    while num2 != 0:
        num3 = num1 % num2
        num1, num2 = num2, num3

    return (question, str(num1))
