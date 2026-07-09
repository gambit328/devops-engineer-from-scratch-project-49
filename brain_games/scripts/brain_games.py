import prompt


def main():
    print("Welcome to the Brain Games!")
    name_user = prompt.string("May I have your name? ")
    print("Hello, " + name_user)


if __name__ == "__main__":
    main()
