from random import choice
from typing import Literal

TEMP_PLAY = ['камень', 'ножницы', 'бумага']
def random_unit_of_game() -> str:
    return choice(TEMP_PLAY)

# логика игры
def game_ruls(player_figure: Literal['камень', 'ножницы', 'бумага'],
              copm_figure: Literal['камень', 'ножницы', 'бумага']) -> bool|None:
    if player_figure == 'камень':
        if copm_figure == 'ножницы':
            return True
        elif copm_figure == 'бумага':
            return False
    elif player_figure == 'ножницы':
        if copm_figure == 'камень':
            return False
        elif copm_figure == 'бумага':
            return True
    elif player_figure == 'бумага':
        if copm_figure == 'камень':
            return True
        elif copm_figure == 'ножницы':
            return False