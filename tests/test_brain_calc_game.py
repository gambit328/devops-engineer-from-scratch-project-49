from brain_games.games.brain_calc_game import (
    get_questions,
    get_task,
    generate_question,
)


def test_get_questions(monkeypatch):
    numbers = iter([5, 2, 0, 1, 3, 1, 2, 3, 2])

    monkeypatch.setattr(
        "brain_games.games.brain_calc_game.randint", lambda a, b: next(numbers)
    )

    assert get_questions() == [("5 + 2", "7"), ("1 - 3", "-2"), ("2 * 3", "6")]


def test_get_task():
    assert get_task() == "What is the result of the expression?"


def test_generate_question():
    assert generate_question(5, 2, "+") == ("5 + 2", "7")
    assert generate_question(1, 3, "-") == ("1 - 3", "-2")
    assert generate_question(2, 3, "*") == ("2 * 3", "6")
