from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from keyboards.default.start_kb import navigating_bot_kb

from loader import dp


@dp.message_handler(Command("info"), state=None)
async def bot_start(message: types.Message):
    await message.answer(f'''Данный раздел находится в разработке!''', reply_markup=navigating_bot_kb)