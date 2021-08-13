from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp, db
from markups.inline.calendar import InlineCalendar
from markups.text import buttons, menu
from states import Menus


@dp.message_handler(Text(equals=buttons.edit_holidays_btn.text), state=[Menus.settings_submenu, None])
async def open_calendar(message: Message, state: FSMContext):
    await Menus.calendar.set()
    await message.answer(text="Редактирование выходных.", reply_markup=menu.edit_calendar_submenu)
    user_id = message.from_user.id
    key = 'calendar_id' + str(user_id)
    async with state.proxy() as data:
        data[user_id] = await db.get_user_holidays(user_id)
        cal_msg = await message.answer(text='Отметьте выходыне:',
                                       reply_markup=await InlineCalendar()(storage=data[user_id]))
        data[key] = cal_msg.message_id
