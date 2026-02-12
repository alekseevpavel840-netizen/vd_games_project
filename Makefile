# Makefile для автоматизации команд проекта vd-games

install:  ## Установить зависимости (uv sync)
	uv sync

VD-games:  ## Запустить игру через точку входа
	uv run vd-start

build:  ## Собрать дистрибутив (wheel + source distribution)
	uv build

package-install:  ## Установить собранный пакет глобально
	uv tool install dist/*.whl
