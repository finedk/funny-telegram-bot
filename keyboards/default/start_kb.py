from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

navigating_bot_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Клавиатура для управления ботом")
        ], 
        [ 
            KeyboardButton("/start"),
            KeyboardButton("/commands")
        ], 
        [ 
            KeyboardButton("/info"),
            KeyboardButton("/cancel")
        ]
    ], 
    resize_keyboard=True
)