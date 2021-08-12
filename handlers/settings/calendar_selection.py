from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from loader import dp
from markups.inline.calendar import InlineCalendar, calendar_cb
from states import Menus


@dp.callback_query_handler(calendar_cb.filter(), state=Menus.calendar)
async def calendar_selection(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    await callback_query.answer(text=None)
    await Menus.calendar.set()
    selected, date = await InlineCalendar.selection(callback_query, callback_data)
    user_id = callback_query.from_user.id
    async with state.proxy() as data:
        if selected:
            data['cb_query_id'] = callback_query.id
            stamp = int(date.timestamp())
            if stamp in data[user_id]:
                data[user_id].pop(data[user_id].index(stamp))
            else:
                data[user_id].append(stamp)
        if date is not None:
            await callback_query.message.edit_reply_markup(
                reply_markup=await InlineCalendar()(data[user_id], int(date.year), int(date.month),
                                                    int(date.day))
            )
