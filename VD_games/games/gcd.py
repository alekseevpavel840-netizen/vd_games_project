"""Игра «НОД»."""
import random
import math

RULE = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    """Возвращает два числа и их НОД."""
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct = math.gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, str(correct)
