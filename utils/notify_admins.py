import logging

from aiogram import Dispatcher

from data.config import who_need_notif


async def on_startup_notify(dp: Dispatcher):
    for admin in who_need_notif:
        try:
            await dp.bot.send_message(admin, f"❗️ Бот был перезапущен!")

        except Exception as err:
            logging.exception(err)
