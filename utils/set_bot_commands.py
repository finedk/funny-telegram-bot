from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("info", "Информация о боте"),
            types.BotCommand("commands", "Список доступных команд"),
            types.BotCommand("cancel", "Остановить текущее действие")
            #types.BotCommand("get_sticker_id", "Получить ID стикера")
        ]
    )
