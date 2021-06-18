from typing import Text, Type
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.types import message
from middlewares.states.all_states import ping_state
from pythonping import ping


from loader import dp

@dp.message_handler(text="/cancel", state=ping_state)
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("✅ Функция остановлена!\n\nВведите новую команду /commands")
    await state.finish()

@dp.message_handler(Command("ping"), state=None)
async def ping_func(message: types.Message, state: FSMContext):
    await message.answer("❗️ Из-за технических ограничений сервиса Heroku функция Ping не работает!")
"""
    await message.answer('''Вы зашли в функцию по работе с ping запросами.\n
Введите IP или Domain адрес, чтобы сделать ping запрос\n
❗️ Все домены и ip адреса, которые вы будете сюда скидывать автоматически будут обрабатываться в этой функции.
❗️ Если вам нужно её остановить, то введите /cancel''')
    await ping_state.step1.set()
"""

@dp.message_handler(content_types="text", state=ping_state.step1)
async def this_func(message: types.Message, state: FSMContext):
    await message.answer("✅ Ваш запрос принят, подождите некоторое время!\n\nСвязи с установленными ограничениями время ожидания может увеличиться до 1 минуты!\n❗️ Во время обработки вы не можете отменить запрос!")
    try:
        res = ping(message.text, timeout=5, size=1024, count=10, df=True)
        await message.reply(f'''📃 Результаты ping запроса на {message.text}:

Задержки:
    Минимальная задержка  -  {res.rtt_min_ms} ms
    Средняя задержка -  {res.rtt_avg_ms} ms
    Максимальная задержка -  {res.rtt_max_ms} ms
Потери:  {int(res.packets_lost * 10)} из 10 пакетов
Фрагментация IP:  не фрагментируется
Размер пакета:  1024 байт
Количество пакетов:  10
Максимальное время ожидания:  5 секунд''')

    except:
        await message.reply("❗️ Проверьте ваш IP/Domain адрес, он неверен!")
