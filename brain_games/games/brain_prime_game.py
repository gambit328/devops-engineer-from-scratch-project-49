from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    number = randint(0, 99)
    correct_answer = "yes" if is_prime(number) else "no"
    question, correct_answer = number, correct_answer

    return question, correct_answer


def is_prime(number):
    if number < 2 or (number > 2 and number % 2 == 0):
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True
