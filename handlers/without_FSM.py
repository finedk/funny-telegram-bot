from typing import Text, Type
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import message, ContentTypes
from middlewares.states import all_states
from keyboards.default.start_kb import navigating_bot_kb


from loader import dp

@dp.message_handler(Command("cancel"))
async def cancel_handler(message: types.Message):
    await message.answer("❗️ Нечего останавливать")

@dp.message_handler(content_types=["photo", "document", "text", "sticker"])
async def without_FSM(message: types.Message):
    """
    Обработчик на случай если бот перезапустится, а у меня нет базы данных для хранения FSM,
    то пользователю отправится это сообщение 
    """
    await message.answer("❗️ Команда не введена!\n\nВозможно это из-за того, что бот был перезагружен\nВведите команду ещё раз!")
