from brain_games.games.brain_prime_game import get_questions, get_task, is_prime


def test_get_questions(monkeypatch):
    numbers = iter([1, 2, 7])

    monkeypatch.setattr(
        "brain_games.games.brain_prime_game.randint", lambda a, b: next(numbers)
    )

    assert get_questions() == [(1, "no"), (2, "yes"), (7, "yes")]


def test_get_task():
    assert (
        get_task()
        == 'Answer "yes" if given number is prime. Otherwise answer "no".'
    )


def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(77) is False
