"""Движок для запуска игр."""
import prompt

ROUNDS_COUNT = 3


def run_game(game):
    """
    Запускает игру.

    Аргументы:
        game: модуль игры, должен содержать функцию get_question_and_answer(),
              которая возвращает кортеж (question, correct_answer).
    """
    print("Welcome to the VD games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    # Печатаем правило игры, если оно есть
    if hasattr(game, "RULE"):
        print(game.RULE)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
