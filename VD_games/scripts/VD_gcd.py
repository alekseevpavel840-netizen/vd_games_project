"""Точка входа для игры «НОД»."""
from VD_games.games import engine, gcd

def main():
    engine.run_game(gcd)

if __name__ == "__main__":
    main()
