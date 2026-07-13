from random import randint


def get_questions():
    questions = []

    for _ in range(3):
        start_num = randint(0, 50)
        step = randint(3, 10)
        secret_num = randint(0, 9)

        question, correct_answer = generate_question(
            start_num, step, secret_num
        )
        questions.append((question, correct_answer))

    return questions


def get_task():
    return "What number is missing in the progression?"


def generate_question(start_num, step, secret_num):
    question = [str(start_num + i * step) for i in range(10)]
    correct_answer = question[secret_num]
    question[secret_num] = ".."

    return " ".join(question), str(correct_answer)
