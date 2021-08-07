from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from markups.text import menu, buttons
from loader import dp


@dp.message_handler(Text(equals=buttons.settings_btn.text), state=None)
async def settings_submenu(message: Message):
    await message.answer(f"Что имеено вы хотите сделать?", reply_markup=menu.settings_submenu)
