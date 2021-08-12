from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus
from utilities import count_weekdays_by_month


@dp.message_handler(Text(equals=buttons.first_view_btn.text), state=[Menus.represent_submenu, None])
async def representation_months(message: Message):
    await Menus.representation_months.set()
    weekdays = await count_weekdays_by_month(message.from_user.id)
    output = ''
    for mon, icon in zip(weekdays, ('🍁', '🍂', '☁️', '🎄',  '☃️', '❄️', '🌱', '🌷', '🌳')):
        week = '|-----------------------------------------------------------------|\n '
        for day in weekdays[mon]:
            week += f"<i> {day}:</i> <i><b>{weekdays[mon][day]}</b></i>"
        week += '\n|-----------------------------------------------------------------|'
        output += f"{icon} <i>{mon.upper()}</i>:\n{week}\n\n"
    await message.answer(f"<i><b>2 0 2 1 — 2 0 2 2</b></i>\n<b>Кол-во дней недели за учебный год по месяцам📚:</b>\n\n{output}",
                         reply_markup=menu.go_back_submenu)
