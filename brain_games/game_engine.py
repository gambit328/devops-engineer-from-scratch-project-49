from brain_games.cli import welcome_user
import prompt


def game_run(questions, task):
    username = welcome_user()
    print(task)
    for question, correct_answer in questions:
        print(f"Question: {question}")
        user_answer = answer_from_user()
        if not is_correct_answer(user_answer, correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'"
            )
            print(f"Let's try again, {username}")
            return
        print("Correct!")
    print(f"Congratulations, {username}!")


def answer_from_user() -> str:
    user_answer = prompt.string("Your answer: ")
    return str(user_answer)


def is_correct_answer(user_answer: str, correct_answer: str) -> bool:
    return True if user_answer == correct_answer else False
