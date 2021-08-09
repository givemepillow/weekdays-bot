from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.inline.calendar import InlineCalendar
from markups.text import menu, buttons
from states import Menus

calendar = InlineCalendar()


@dp.message_handler(Text(equals=buttons.edit_holidays_btn.text), state=[Menus.settings_submenu, None])
async def open_calendar_handler(message: Message):
    await Menus.calendar.set()
    await message.answer(text="Редактирование выходных.", reply_markup=menu.edit_calendar_submenu)
    await message.answer(text='Отметьте выходыне:', reply_markup=await calendar())
