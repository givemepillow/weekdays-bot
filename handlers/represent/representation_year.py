from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from prettytable import PrettyTable
from loader import dp
from markups.text import menu, buttons
from states import Menus
from utilities import count_year_weekdays


@dp.message_handler(Text(equals=buttons.second_view_btn.text), state=[Menus.represent_submenu, None])
async def representation_one(message: Message):
    await Menus.representation_months.set()
    weekdays = await count_year_weekdays(message.from_user.id)
    output = '|--------------------------|\n'
    for k in weekdays:
        output += f"| • <i>{k}</i>: <b>{weekdays[k]}</b> шт. 📌 \n"
        output += f"|--------------------------|\n"
    await message.answer(f"<i><b>2 0 2 1 — 2 0 2 2</b></i>\n<b>Кол-во дней недели за учебный год 📚:</b>\n{output}", reply_markup=menu.go_back_submenu)
