from brain_games.games.brain_even_game import get_questions, get_task


def test_get_questions(monkeypatch):
    numbers = iter([4, 5, 8])

    monkeypatch.setattr(
        "brain_games.games.brain_even_game.randint", lambda a, b: next(numbers)
    )

    assert get_questions() == [(4, "yes"), (5, "no"), (8, "yes")]


def test_get_task():
    assert (
        get_task()
        == 'Answer "yes" if the number is even, otherwise answer "no".'
    )
