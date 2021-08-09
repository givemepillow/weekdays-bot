from markups.inline.calendar import InlineCalendar, calendar_cb, storage
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus

calendar = InlineCalendar()


@dp.message_handler(Text(equals=buttons.edit_holidays_btn.text), state=Menus.settings_submenu)
async def open_calendar_handler(message: Message):
    await message.answer("Отметье выходные: ", reply_markup=await calendar())
