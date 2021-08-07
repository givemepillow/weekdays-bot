from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus


@dp.message_handler(Text(equals=buttons.add_holidays_btn.text), state=Menus.settings_submenu)
async def add_holidays_submenu(message: Message):
    await Menus.add_holidays_submenu.set()
    await message.answer(f"Каким образом?", reply_markup=menu.add_holidays_submenu)
