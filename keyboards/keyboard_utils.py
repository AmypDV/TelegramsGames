from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Создаем объекты кнопок старта
startgame_button = KeyboardButton(text='Сыграем')
help_button = KeyboardButton(text='Помощь')

# Инициализируем объект билдера
kb_builder_startgame = ReplyKeyboardBuilder()
kb_builder_startgame.row(startgame_button, help_button, width=1)
keyboard_start_game: ReplyKeyboardMarkup = kb_builder_startgame.as_markup(
                                               resize_keyboard=True,
                                               is_persistent=True,
                                               one_time_keyboard=False,
                                               input_field_placeholder='Ничего писать не нужно'
                                               )

# Создаем объекты кнопок игры
scissors_button = KeyboardButton(text='ножницы')
stone_button = KeyboardButton(text='камень')
paper_button = KeyboardButton(text='бумага')

# Инициализируем объект билдера игры
kb_builder_game = ReplyKeyboardBuilder()
kb_builder_game.row(stone_button, scissors_button, paper_button, width=3)
keyboard_game: ReplyKeyboardMarkup = kb_builder_game.as_markup(
                                        resize_keyboard=True,
                                        is_persistent=True,
                                        one_time_keyboard=False,
                                        input_field_placeholder='Ничего писать не нужно'
                                        )

next_game_button = KeyboardButton(text='Продолжить игру')
end_game_button = KeyboardButton(text='Закончить игру')

# Инициализируем объект билдера игры
kb_builder_next_game = ReplyKeyboardBuilder()
kb_builder_next_game.row(next_game_button, end_game_button, width=2)
keyboard_next_game: ReplyKeyboardMarkup = kb_builder_next_game.as_markup(
                                        resize_keyboard=True,
                                        is_persistent=True,
                                        one_time_keyboard=False,
                                        input_field_placeholder='Ничего писать не нужно'
                                        )




