from brain_games.brain_even_game import (
    quest_generator,
    get_string_for_end,
    get_string,
    question_answer_and_result,
    is_correct_answer,
)


def test_quest_generator():
    assert len(quest_generator()) == 3


def test_get_string():
    assert (
        get_string("yes") == "'yes' is wrong answer ;(. Correct answer was 'no'"
    )
    assert (
        get_string("no") == "'no' is wrong answer ;(. Correct answer was 'yes'"
    )
    assert get_string("correct") == "Correct!"


def test_get_string_for_end():
    expected_win = "Congratulations, Bill!"
    expected_lose = "Let's try again, Bill!"
    assert get_string_for_end("Bill", True) == expected_win
    assert get_string_for_end("Bill", False) == expected_lose


def test_is_correct_answer():
    assert is_correct_answer("yes", "yes") is True
    assert is_correct_answer("no", "no") is True
    assert is_correct_answer("no", "yes") is False
    assert is_correct_answer("yes", "no") is False


def test_question_answer_and_result_is_correct(monkeypatch):
    user_answers = iter(["yes", "no", "yes"])
    questions = [(4, "yes"), (9, "no"), (8, "yes")]

    monkeypatch.setattr(
        "brain_games.brain_even_game.answer_from_user",
        lambda: next(user_answers),
    )

    assert question_answer_and_result(questions) is True


def test_question_answer_and_result_is_wrong(monkeypatch):
    user_answers = iter(["yes", "yes", "yes"])
    questions = [(4, "yes"), (9, "no"), (8, "yes")]

    monkeypatch.setattr(
        "brain_games.brain_even_game.answer_from_user",
        lambda: next(user_answers),
    )

    assert question_answer_and_result(questions) is False
