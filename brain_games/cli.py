import prompt


def welcome_user() -> str:
    print("Welcome to the Brain Games!")
    name_user = prompt.string("May I have your name? ")
    print(f"Hello, {name_user}!")
    return str(name_user)
