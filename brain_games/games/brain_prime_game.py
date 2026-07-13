from random import randint


def get_questions():
    questions = []

    for _ in range(3):
        number = randint(0, 99)
        correct_answer = "yes" if is_prime(number) else "no"
        questions.append((number, correct_answer))

    return questions


def get_task():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2 or (number > 2 and number % 2 == 0):
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True
