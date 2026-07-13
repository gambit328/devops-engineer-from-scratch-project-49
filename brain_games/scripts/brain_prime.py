from brain_games.games.brain_prime_game import get_questions, get_task
from brain_games.game_engine import game_run


def main():
    game_run(get_questions(), get_task())


if __name__ == "__main__":
    main()
