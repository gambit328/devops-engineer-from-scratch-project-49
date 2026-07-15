from brain_games.cli import welcome_user
import prompt

ROUNDS = 3


def game_run(game):
    username = welcome_user()
    print(game.TASK)

    for _ in range(ROUNDS):
        question, correct_answer = game.get_question()
        print(f"Question: {question}")

        user_answer = answer_from_user()
        if not is_correct_answer(user_answer, correct_answer):
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'"
            )
            print(f"Let's try again, {username}!")
            return
        print("Correct!")

    print(f"Congratulations, {username}!")


def answer_from_user() -> str:
    user_answer = prompt.string("Your answer: ")
    return str(user_answer)


def is_correct_answer(user_answer: str, correct_answer: str) -> bool:
    return True if user_answer == correct_answer else False
