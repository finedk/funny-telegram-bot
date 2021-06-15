from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_kb import navigating_bot_kb

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'''👋 Привет, {message.from_user.username}!

📃 Чтобы получить список доступных команд,\nвам нужно ввести /commands''', reply_markup=navigating_bot_kb)
