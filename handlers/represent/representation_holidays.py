from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus
from utilities import holidays


@dp.message_handler(Text(equals=buttons.holidays_btn.text), state=[Menus.represent_submenu, None])
async def representation_holidays(message: Message):
    await Menus.representation_holidays.set()
    days = await holidays(message.from_user.id)
    output = ''
    if days == {}:
        output = "<i>Выходные не установлены.</i>"
    else:
        for m in days:
            month = ''
            for d in days[m]:
                month += f"<b>{d}</b>, "
            output += f"🎉 <i><b>{m}:</b></i>\n{month[0:-2]}"
            output += '\n\n'
    await message.answer(f"<b><i>Установленные выходные:</i></b>\n\n{output}", reply_markup=menu.go_back_submenu)
