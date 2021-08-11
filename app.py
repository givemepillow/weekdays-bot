from aiogram import executor

from handlers import dp
from loader import bot, storage, db


async def on_shutdown(*args):
    await bot.close()
    await storage.close()


async def on_startup(*args):
    await db.create()


if __name__ == '__main__':
    executor.start_polling(
        on_shutdown=on_shutdown,
        on_startup=on_startup,
        skip_updates=True,
        dispatcher=dp
    )
