from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus


@dp.message_handler(Text(equals=buttons.yes_btn.text), state=Menus.are_u_sure)
async def reset_complete(message: Message):
    await Menus.reset_complete.set()
    await message.answer(f"Все выходные сброшены.", reply_markup=menu.go_back_submenu)
