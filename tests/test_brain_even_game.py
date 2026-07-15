from brain_games.games.brain_even_game import get_question


def test_get_questions(monkeypatch):
    numbers = iter([5])

    monkeypatch.setattr(
        "brain_games.games.brain_even_game.randint", lambda a, b: next(numbers)
    )

    assert get_question() == (5, "no")
