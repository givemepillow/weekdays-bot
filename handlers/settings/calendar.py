from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery

from loader import dp
from markups.inline.calendar import InlineCalendar, calendar_cb
from markups.text import buttons, menu
from states import Menus

calendar = InlineCalendar()


@dp.message_handler(Text(equals=buttons.edit_holidays_btn.text), state=[Menus.settings_submenu, None])
async def open_calendar(message: Message, state: FSMContext):
    await Menus.calendar.set()
    await message.answer(text="Редактирование выходных.", reply_markup=menu.go_back_submenu)
    user_id = message.from_user.id
    async with state.proxy() as data:
        if user_id not in data.keys():
            data[user_id] = []
        cal_msg = await message.answer(text='Отметьте выходыне:',
                                       reply_markup=await calendar(storage=data[user_id]))
        data['calendar_id'] = cal_msg.message_id


@dp.callback_query_handler(calendar_cb.filter(), state=Menus.calendar)
async def calendar_selection(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    await Menus.calendar.set()
    selected, date = await InlineCalendar.selection(callback_query, callback_data)
    user_id = callback_query.from_user.id
    async with state.proxy() as data:
        if selected:
            stamp = int(date.timestamp())
            if stamp in data[user_id]:
                data[user_id].pop(data[user_id].index(stamp))
            else:
                data[user_id].append(stamp)
        if date is not None:
            await callback_query.message.edit_reply_markup(
                reply_markup=await calendar(data[user_id], int(date.year), int(date.month),
                                            int(date.day))
            )
