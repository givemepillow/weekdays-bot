from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus


@dp.message_handler(Text(equals=buttons.reset_holidays_btn.text), state=Menus.settings_submenu)
async def confirmation(message: Message):
    await Menus.are_u_sure.set()
    await message.answer(f"⚠️ Вы вы точно хотите очистить календарь?", reply_markup=menu.are_u_sure_submenu)
