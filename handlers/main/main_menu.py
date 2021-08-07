from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message

from markups.text import menu, buttons
from loader import dp


@dp.message_handler(Text(equals=buttons.main_menu_btn.text), state='*')
@dp.message_handler(Command("start"), state='*')
async def main_menu(message: Message):
    await message.answer("Главное меню. Выбирете что хотите сделать:", reply_markup=menu.main_menu)
