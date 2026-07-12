from random import randint


def get_questions() -> list:
    result = []
    for _ in range(3):
        num = randint(1, 20)
        correct_answer = "yes" if num % 2 == 0 else "no"
        result.append((num, correct_answer))
    return result


def get_task() -> str:
    return 'Answer "yes" if the number is even, otherwise answer "no".'
