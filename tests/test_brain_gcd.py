from brain_games.games.brain_gcd_game import (
    get_questions,
    get_task,
    generate_question,
)


def test_get_questions(monkeypatch):
    numbers = iter([25, 50, 100, 52, 3, 9])

    monkeypatch.setattr(
        "brain_games.games.brain_gcd_game.randint", lambda a, b: next(numbers)
    )

    assert get_questions() == [("50 25", "25"), ("100 52", "4"), ("9 3", "3")]


def test_get_task():
    assert get_task() == "Find the greatest common divisor of given numbers"


def test_generate_question():
    assert generate_question(50, 25) == ("50 25", "25")
