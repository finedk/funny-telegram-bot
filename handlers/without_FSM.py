from typing import Text, Type
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import message, ContentTypes
from middlewares.states import all_states


from loader import dp

@dp.message_handler(content_types=["photo", "document", "text"])
async def without_FSM(message: types.Message):
    await message.answer("❗️ Команда не введена")
