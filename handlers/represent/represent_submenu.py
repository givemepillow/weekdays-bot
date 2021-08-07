from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from markups.text import menu, buttons
from loader import dp


@dp.message_handler(Text(equals=buttons.represent_btn.text), state=None)
async def represent_submenu(message: Message):
    await message.answer(f"В каком виде представить данные?", reply_markup=menu.represent_submenu)
