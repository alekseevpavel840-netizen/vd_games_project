"""Игра «Калькулятор»."""
import random
import operator

RULE = "What is the result of the expression?"


def get_question_and_answer():
    """Возвращает вопрос (выражение) и правильный ответ."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    else:  # *
        result = num1 * num2

    question = f"{num1} {op} {num2}"
    return question, str(result)
