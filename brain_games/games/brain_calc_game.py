from random import randint

TASK = "What is the result of the expression?"


def get_question():
    operations = ["+", "-", "*"]

    num1 = randint(0, 50)
    num2 = randint(0, 50)
    operation = operations[randint(0, 2)]

    question, correct_answer = generate_question(num1, num2, operation)

    return question, correct_answer


def generate_question(num1, num2, operation):
    correct_answer = 0

    match operation:
        case "+":
            correct_answer += num1 + num2
        case "-":
            correct_answer += num1 - num2
        case "*":
            correct_answer += num1 * num2

    question = f"{num1} {operation} {num2}"

    return question, str(correct_answer)
