"""Точка входа для игры «Чётность»."""

from VD_games.engine import run_game
from VD_games.games import even

if __name__ == '__main__':
    run_game(even)
