from typing import Text, Type
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import message
from middlewares.states.all_states import sticker_state

from loader import dp

@dp.message_handler(text="/cancel", state=sticker_state)
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("✅ Функция остановлена!\n\nВведите новую команду /commands")
    await state.finish()

@dp.message_handler(Command("get_sticker_id"), state=None)
async def get_sticker_id(message: types.Message):
    await message.answer('''Вы зашли в функцию по получению ID стикера.\n
Скиньте стикер боту!\n
❗️ Всё, что вы будете сюда скидывать автоматически будут обрабатываться в этой функции.
❗️ Если вам нужно её остановить, то введите /cancel''')
    await sticker_state.step1.set()

@dp.message_handler(content_types="sticker", state=sticker_state.step1)
async def get_sticker_id_send(message: types.Message):
    await message.reply("ID этого стикера - ")
    await message.answer(message.sticker.file_id)
