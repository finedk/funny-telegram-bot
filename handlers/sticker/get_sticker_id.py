from typing import Text, Type
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import message

from loader import dp

@dp.message_handler(Command("get_sticker_id"))
async def get_sticker_id(message: types.Message):
    await message.answer("Скиньте стикер")

@dp.message_handler(content_types="sticker")
async def get_sticker_id_send(message: types.Message):
    await message.reply("ID этого стикера - ")
    await message.answer(message.sticker.file_id)
