from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus


@dp.message_handler(Text(equals=[buttons.represent_btn.text, buttons.go_back_btn.text]),
                    state=[Menus.main_menu, Menus.representation_months,
                           Menus.representation_months,
                           Menus.representation_holidays,
                           None
                           ])
async def represent_submenu(message: Message):
    await Menus.represent_submenu.set()
    await message.answer(f"В каком виде представить данные?", reply_markup=menu.represent_submenu)
