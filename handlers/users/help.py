from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, CommandHelp

from loader import dp

@dp.message_handler(Command("commands"))
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = '''Список доступных команд:

Служебные команды:
/start - Запустить бота
/info - Информация о боте
/commands - Список доступных команд
/cancel - Остановить текущее действие

Доступные функции:
/get_sticker_id - Получить ID стикера
/download_sticker - Скачать стикер в фомате PNG
/gender_person_in_photo - Узнать пол человека на фото
/ping - Сделать Ping запрос к IP с полной информацией'''
    

    await message.answer(text)
