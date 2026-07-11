from random import randint


def get_random_number_from_to(min_num: int, max_num: int) -> int:
    return randint(min_num, max_num)


def get_random_number_to(max_num: int) -> int:
    return randint(0, max_num)
