from brain_games.brain_even_game import (
    quest_generator,
    question_answer_and_result,
    get_string_for_end,
)
from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    questions = quest_generator()
    print("'yes' if the number is even, otherwise answer 'no'.")
    flag = question_answer_and_result(questions)
    print(get_string_for_end(user_name, flag))


if __name__ == "__main__":
    main()
