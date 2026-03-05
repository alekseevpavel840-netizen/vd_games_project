"""Точка входа для игры «Калькулятор»."""
from VD_games.games import engine, calc

def main():
    engine.run_game(calc)

if __name__ == "__main__":
    main()
