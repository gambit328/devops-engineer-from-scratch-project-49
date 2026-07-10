import prompt
from random import randint


def quest_generator() -> list:
    result = []
    for _ in range(3):
        num = randint(1, 20)
        correct_answer = "yes" if num % 2 == 0 else "no"
        result.append((num, correct_answer))
    return result


def answer_from_user() -> str:
    user_answer = prompt.string("Your answer: ")
    return str(user_answer)


def is_correct_answer(user_answer: str, correct_answer: str) -> bool:
    return True if user_answer == correct_answer else False


def question_answer_and_result(questions: list) -> bool:
    for question, correct_answer in questions:
        print(f"Question: {question}")
        user_answer = answer_from_user()
        if is_correct_answer(user_answer, correct_answer):
            print(get_string("correct"))
        else:
            print(get_string(user_answer))
            return False

    return True


def get_string(user_answer):
    vault_strings = {
        "yes": "'yes' is wrong answer ;(. Correct answer was 'no'",
        "no": "'no' is wrong answer ;(. Correct answer was 'yes'",
        "correct": "Correct!",
    }
    return vault_strings[user_answer]


def get_string_for_end(user_name: str, flag: bool) -> str:
    result = (
        f"Congratulations, {user_name}!"
        if flag
        else f"Let's try again, {user_name}!"
    )

    return result
