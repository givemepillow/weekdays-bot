from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from states import Menus
from markups.text import menu, buttons
from loader import dp


@dp.message_handler(Text(equals=buttons.represent_btn.text), state=Menus.main_menu)
async def represent_submenu(message: Message):
    await Menus.represent_submenu.set()
    await message.answer(f"В каком виде представить данные?", reply_markup=menu.represent_submenu)
