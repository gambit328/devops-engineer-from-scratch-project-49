from brain_games.games.brain_progression_game import (
    get_questions,
    get_task,
    generate_question,
)


def test_get_questions(monkeypatch):
    numbers = iter([5, 2, 5, 2, 3, 3, 14, 5, 9])

    monkeypatch.setattr(
        "brain_games.games.brain_progression_game.randint",
        lambda a, b: next(numbers),
    )

    assert get_questions() == [
        ("5 7 9 11 13 .. 17 19 21 23", "15"),
        ("2 5 8 .. 14 17 20 23 26 29", "11"),
        ("14 19 24 29 34 39 44 49 54 ..", "59"),
    ]


def test_get_task():
    assert get_task() == "What number is missing in the progression?"


def test_generate_question():
    assert generate_question(5, 2, 5) == ("5 7 9 11 13 .. 17 19 21 23", "15")
