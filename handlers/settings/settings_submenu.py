from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus


@dp.message_handler(Text(equals=buttons.go_back_btn.text), state=[Menus.add_holidays_submenu])
@dp.message_handler(Text(equals=buttons.settings_btn.text), state=[Menus.main_menu])
async def settings_submenu(message: Message):
    await Menus.settings_submenu.set()
    await message.answer(f"Что имеено вы хотите сделать?", reply_markup=menu.settings_submenu)
