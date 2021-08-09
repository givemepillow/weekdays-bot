from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from loader import dp
from markups.inline.calendar import InlineCalendar, calendar_cb, temp_storage
from markups.text import menu, buttons
from states import Menus

calendar = InlineCalendar()


@dp.message_handler(Text(equals=buttons.edit_holidays_btn.text), state=[Menus.settings_submenu, None])
async def open_calendar(message: Message):
    await Menus.calendar.set()
    await message.answer(text="Редактирование выходных.", reply_markup=menu.edit_calendar_submenu)
    await message.answer(text='Отметьте выходыне:', reply_markup=await calendar())


@dp.callback_query_handler(calendar_cb.filter(), state=Menus.calendar)
async def calendar_selection(callback_query: CallbackQuery, callback_data: dict):
    selected, date = await InlineCalendar.selection(callback_query, callback_data)
    if selected:
        stamp = int(date.timestamp())
        if stamp in temp_storage:
            temp_storage.pop(temp_storage.index(stamp))
        else:
            temp_storage.append(stamp)
    if date is not None:
        await callback_query.message.edit_reply_markup(
            reply_markup=await calendar(int(date.year), int(date.month), int(date.day))
            )
