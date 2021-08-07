from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus


@dp.message_handler(Text(equals=buttons.go_back_btn.text), state=[Menus.settings_submenu, Menus.represent_submenu])
@dp.message_handler(Command("start"), state='*')
async def main_menu(message: Message):
    await message.answer("Главное меню. Выбирете что хотите сделать:", reply_markup=menu.main_menu)
    await Menus.main_menu.set()
