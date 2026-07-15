from brain_games.games.brain_calc_game import (
    get_question,
    generate_question,
)


def test_get_questions(monkeypatch):
    numbers = iter([5, 2, 0])

    monkeypatch.setattr(
        "brain_games.games.brain_calc_game.randint", lambda a, b: next(numbers)
    )

    assert get_question() == ("5 + 2", "7")


def test_generate_question():
    assert generate_question(5, 2, "+") == ("5 + 2", "7")
    assert generate_question(1, 3, "-") == ("1 - 3", "-2")
    assert generate_question(2, 3, "*") == ("2 * 3", "6")
