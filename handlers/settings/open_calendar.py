from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.inline.calendar import InlineCalendar
from markups.text import buttons, menu
from states import Menus


@dp.message_handler(Text(equals=buttons.edit_holidays_btn.text), state=[Menus.settings_submenu, None])
async def open_calendar(message: Message, state: FSMContext):
    await Menus.calendar.set()
    await message.answer(text="Редактирование выходных.", reply_markup=menu.go_back_submenu)
    user_id = message.from_user.id
    async with state.proxy() as data:
        if user_id not in data.keys():
            data[user_id] = []
        cal_msg = await message.answer(text='Отметьте выходыне:',
                                       reply_markup=await InlineCalendar()(storage=data[user_id]))
        data['calendar_id'] = cal_msg.message_id
