from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from loader import dp
from markups.inline.calendar import InlineCalendar, calendar_cb, temp_storage
from markups.text import buttons, menu
from states import Menus

calendar = InlineCalendar()


@dp.message_handler(Text(equals=buttons.edit_holidays_btn.text), state=[Menus.settings_submenu, None])
async def open_calendar(message: Message, state: FSMContext):
    await Menus.calendar.set()
    await message.answer(text="Редактирование выходных.", reply_markup=menu.go_back_submenu)
    cal_msg = await message.answer(text='Отметьте выходыне:', reply_markup=await calendar())
    async with state.proxy() as data:
        data['calendar_id'] = cal_msg.message_id


@dp.callback_query_handler(calendar_cb.filter(), state=Menus.calendar)
async def calendar_selection(callback_query: CallbackQuery, callback_data: dict):
    await Menus.calendar.set()
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
