from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram import Router

import logging


from filters.text import MyFilterWords
from lexicon.lexicon import LEXICON_RU



logger = logging.getLogger(__name__)

router_user = Router()


# @router_user.message()
# async def send_echo(message: Message):
#     if message.content_type == ContentType.TEXT:
#         await message.reply(text=message.text)
#         logger.info(f'answer text. Member {message.from_user.id}')
#     elif message.content_type == ContentType.STICKER:
#         logger.info(f'answer stiker. Member {message.from_user.id}')
#         await message.answer_sticker(message.sticker.file_id)
#     else:
#         logger.info(f'answer stupid. Member {message.from_user.id}')
#         await message.answer(text=LEXICON_RU().stupid)