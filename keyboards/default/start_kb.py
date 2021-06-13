from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_panel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Узнать ID стикера"),
            KeyboardButton("Узнать пол человека на фото")
        ]
    ], 
    resize_keyboard=True
)