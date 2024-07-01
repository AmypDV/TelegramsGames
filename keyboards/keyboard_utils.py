from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Создаем объекты кнопок старта
startgame_button = KeyboardButton(text='Начинаем игру "Камень, ножницы, бумага"')

# Инициализируем объект билдера
kb_builder_startgame = ReplyKeyboardBuilder()
kb_builder_startgame.add(startgame_button)
keyboard_startgame = kb_builder_startgame.as_markup(
                                               resize_keyboard=True,
                                               one_time_keyboard=True,
                                               input_field_placeholder='Ничего писать не нужно'
                                               )

# Создаем объекты кнопок игры
scissors_button = KeyboardButton(text='ножницы')
stone_button = KeyboardButton(text='камень')
paper_button = KeyboardButton(text='бумага')
endgame_button = KeyboardButton(text='Закончить игру')

# Инициализируем объект билдера игры
kb_builder_game = ReplyKeyboardBuilder()
kb_builder_game.row(stone_button, scissors_button, paper_button, endgame_button, width=3)
keyboard_game = kb_builder_game.as_markup(
                                        resize_keyboard=True,
                                        one_time_keyboard=True,
                                        input_field_placeholder='Ничего писать не нужно'
                                        )



