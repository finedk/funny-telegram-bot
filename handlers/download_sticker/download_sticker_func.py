from typing import Text, Type
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import message
from middlewares.states.all_states import download_sticker_state
import os

from loader import dp

@dp.message_handler(text="/cancel", state=download_sticker_state)
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("✅ Функция остановлена!\n\nВведите новую команду /commands")
    await state.finish()

@dp.message_handler(Command("download_sticker"), state=None)
async def get_sticker_id(message: types.Message):
    await message.answer('''Вы зашли в функцию по загрузке стикера.\n
Скиньте стикер боту!\n
❗️ Всё, что вы будете сюда скидывать автоматически будут обрабатываться в этой функции.
❗️ Если вам нужно её остановить, то введите /cancel''')
    await download_sticker_state.step1.set()

@dp.message_handler(content_types="sticker", state=download_sticker_state.step1)
async def get_sticker_id_send(message: types.Message):
    stickerpack_name = message.sticker.set_name
    sticker_emoji = message.sticker.emoji
    username = message.from_user.username
    await message.sticker.download(f"./handlers/download_sticker/temp/{stickerpack_name} - @{username}.png")
    await message.reply_document(types.InputFile(f"./handlers/download_sticker/temp/{stickerpack_name} - @{username}.png"))
    os.remove(f"./handlers/download_sticker/temp/{stickerpack_name} - @{username}.png")
