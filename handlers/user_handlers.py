from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram import Router, F

import logging

from utils.utils import random_unit_of_game, game_ruls
from keyboards.keyboard_utils import keyboard_game, keyboard_startgame
from lexicon.lexicon import LEXICON_RU
from states.states import Player, PLAYERS



logger = logging.getLogger(__name__)

router_user = Router()


@router_user.message(F.text == 'Начинаем игру "Камень, ножницы, бумага"')
async def start_game(message: Message):
        logger.info(f'start game. Member {message.from_user.id}')
        PLAYERS[message.from_user.id].games_figure = random_unit_of_game()
        PLAYERS[message.from_user.id].n_games += 1
        await message.answer(text='Камень, ножницы или бумага?',
                             reply_markup=keyboard_game
                             )

@router_user.message(F.text.in_(['камень', 'ножницы', 'бумага']))
async def get_stone_in_game(message: Message):
    logger.info(f'get stone. Member {message.from_user.id}')
    if game_ruls(message.text, PLAYERS[message.from_user.id].games_figure) is None:
        await message.answer(text=f'У меня {PLAYERS[message.from_user.id].games_figure}\n'
                                  f'{message.from_user.first_name} у нас ничья!\n'
                                  f'счет {PLAYERS[message.from_user.id].n_wins}:{PLAYERS[message.from_user.id].n_lose}',
                             reply_markup=keyboard_startgame
                             )
    elif game_ruls(message.text, PLAYERS[message.from_user.id].games_figure):
        PLAYERS[message.from_user.id].n_wins += 1
        await message.answer(text=f'У меня {PLAYERS[message.from_user.id].games_figure}\n'
                                  f'{message.from_user.first_name} вы выиграли!\n'
                                  f'счет {PLAYERS[message.from_user.id].n_wins}:{PLAYERS[message.from_user.id].n_lose}',
                             reply_markup=keyboard_startgame
                            )
    elif not game_ruls(message.text, PLAYERS[message.from_user.id].games_figure):
        PLAYERS[message.from_user.id].n_lose += 1
        await message.answer(text=f'У меня {PLAYERS[message.from_user.id].games_figure}\n'
                                  f'{message.from_user.first_name} вы проиграли!\n'
                                  f'счет {PLAYERS[message.from_user.id].n_wins}:{PLAYERS[message.from_user.id].n_lose}',
                             reply_markup=keyboard_startgame
                            )
