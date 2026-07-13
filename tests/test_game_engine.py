import pytest
from brain_games.game_engine import (
    game_run,
    answer_from_user,
    is_correct_answer,
)


@pytest.fixture
def even_questions():
    return [(4, "yes"), (5, "no"), (8, "yes")]


def test_game_run_win(monkeypatch, capsys, even_questions):
    even_task = 'Answer "yes" if the number is even, otherwise answer "no".'
    user_answers = iter(["yes", "no", "yes"])

    monkeypatch.setattr("brain_games.game_engine.welcome_user", lambda: "Bill")

    monkeypatch.setattr(
        "brain_games.game_engine.answer_from_user", lambda: next(user_answers)
    )

    game_run(even_questions, even_task)
    out = capsys.readouterr().out

    assert "Let's try again, Bill!" not in out
    assert "Congratulations, Bill!" in out


def test_game_run_lose(monkeypatch, capsys, even_questions):
    even_task = 'Answer "yes" if the number is even, otherwise answer "no".'
    user_answers = iter(["yes", "yes", "yes"])

    monkeypatch.setattr("brain_games.game_engine.welcome_user", lambda: "Bill")

    monkeypatch.setattr(
        "brain_games.game_engine.answer_from_user", lambda: next(user_answers)
    )

    game_run(even_questions, even_task)
    out = capsys.readouterr().out

    assert "Let's try again, Bill!" in out
    assert "Congratulations, Bill!" not in out


def test_answer_from_user(monkeypatch):
    user_answer = iter(["yes"])
    monkeypatch.setattr(
        "brain_games.game_engine.prompt.string", lambda _: next(user_answer)
    )
    assert answer_from_user() == "yes"


def test_is_correct_answer():
    assert is_correct_answer("yes", "yes") is True
    assert is_correct_answer("no", "yes") is False
