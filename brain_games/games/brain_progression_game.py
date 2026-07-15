from random import randint

TASK = "What number is missing in the progression?"


def get_question():
    start_num = randint(0, 50)
    step = randint(3, 10)
    secret_num = randint(0, 9)

    question, correct_answer = generate_question(start_num, step, secret_num)

    return question, correct_answer


def generate_question(start_num, step, secret_num):
    question = [str(start_num + i * step) for i in range(10)]
    correct_answer = question[secret_num]
    question[secret_num] = ".."

    return " ".join(question), str(correct_answer)
