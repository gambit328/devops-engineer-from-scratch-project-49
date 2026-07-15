from brain_games.games.brain_gcd_game import (
    get_question,
    generate_question,
)


def test_get_questions(monkeypatch):
    numbers = iter([100, 52])

    monkeypatch.setattr(
        "brain_games.games.brain_gcd_game.randint", lambda a, b: next(numbers)
    )

    assert get_question() == ("100 52", "4")


def test_generate_question():
    assert generate_question(50, 25) == ("50 25", "25")
