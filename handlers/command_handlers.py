from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router

from keyboards.keyboard_utils import keyboard_start_game
from states.states import Player, PLAYERS, write_pickle_db

from lexicon.lexicon import LEXICON_RU
import logging


logger = logging.getLogger(__name__)

router_command = Router()

# Этот хэндлер будет срабатывать на команду "/start"
@router_command.message(CommandStart())
async def process_start_command(message: Message):
    logger.info(f'command start. Member {message.from_user.id}')
    id = message.from_user.id
    if id not in PLAYERS:
        name = message.from_user.first_name
        PLAYERS[id] = Player(id_player=id,
                             name_player=name)
        logger.info(f'add player: name {name}, id {id}')
        write_pickle_db(PLAYERS)
    await message.answer(text=LEXICON_RU().start,
                         reply_markup=keyboard_start_game)


# Этот хэндлер будет срабатывать на команду "/help"
@router_command.message(Command(commands='help'))
async def process_help_command(message: Message):
    logger.info(f'command help. Member {message.from_user.id}')
    await message.answer(text=LEXICON_RU().help,
                         reply_markup=keyboard_start_game)