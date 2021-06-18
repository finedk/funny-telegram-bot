from typing import Text, Type
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import message, ContentTypes
from middlewares.states import all_states
from keyboards.default.start_kb import navigating_bot_kb


from loader import dp


@dp.message_handler(Command("on_keyboard"), state="*")
async def on_keyboard(message: types.Message):
    await message.answer("✅ Клавиатура включена!", reply_markup=navigating_bot_kb)

@dp.message_handler(text="Клавиатура для управления ботом", state="*")
async def keyboard_handler(message: types.Message):
    await message.answer("Данная клавиатура нужна для упрощённого взаимодействия с ботом. В ней уже введены команды служебных функций, из-за этого вам не нужно каждый раз нажимать на команду /commands, чтобы вывести список доступных функций!")
