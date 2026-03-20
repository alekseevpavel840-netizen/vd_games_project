"""Модуль с основной игрой VD-games (приветствие)."""

from VD_games.cli import welcome_user

def main():
    """Запускает приветствие игры."""
    print("Welcome to the VD-games!")
    welcome_user()

if __name__ == "__main__":
    main()
