from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram import Router, F

import logging

from utils.utils import random_unit_of_game, game_ruls
from keyboards.keyboard_utils import keyboard_game, keyboard_start_game, keyboard_next_game
from lexicon.lexicon import LEXICON_RU
from states.states import PLAYERS, write_pickle_db



logger = logging.getLogger(__name__)

router_user = Router()


@router_user.message(F.text.in_({'Сыграем', 'Продолжить игру'}))
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
                             reply_markup=keyboard_next_game
                             )
    elif game_ruls(message.text, PLAYERS[message.from_user.id].games_figure):
        PLAYERS[message.from_user.id].n_wins += 1
        await message.answer(text=LEXICON_RU.game_win.format(comp_figure=PLAYERS[message.from_user.id].games_figure,
                                                            first_name=message.from_user.first_name,
                                                            wins=PLAYERS[message.from_user.id].n_wins,
                                                            lose=PLAYERS[message.from_user.id].n_lose),
                             reply_markup=keyboard_next_game
                            )
    elif not game_ruls(message.text, PLAYERS[message.from_user.id].games_figure):
        PLAYERS[message.from_user.id].n_lose += 1
        await message.answer(text=f'У меня {PLAYERS[message.from_user.id].games_figure}\n'
                                  f'{message.from_user.first_name} вы проиграли!\n'
                                  f'счет {PLAYERS[message.from_user.id].n_wins}:{PLAYERS[message.from_user.id].n_lose}',
                             reply_markup=keyboard_next_game
                            )

@router_user.message(F.text == 'Закончить игру')
async def start_game(message: Message):
        logger.info(f'end game. Member {message.from_user.id}')
        PLAYERS[message.from_user.id].n_games += 1
        write_pickle_db(PLAYERS)
        await message.answer(text='До скорых встреч!',
                             reply_markup=keyboard_start_game
                             )

@router_user.message(F.text == 'Помощь')
async def start_game(message: Message):
        logger.info(f'/help. Member {message.from_user.id}')
        await message.answer(text=LEXICON_RU.help,
                             reply_markup=keyboard_start_game)