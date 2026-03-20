"""Точка входа для игры «Калькулятор»."""

from VD_games.engine import run_game
from VD_games.games import calc

if __name__ == '__main__':
    run_game(calc)
