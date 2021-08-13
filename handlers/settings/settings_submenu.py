from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp, bot, db
from markups.text import menu, buttons
from states import Menus


@dp.message_handler(Text(equals=[buttons.go_back_btn.text, buttons.no_btn.text, buttons.edit_holidays_save_btn.text,
                                 buttons.edit_holidays_cancel_btn.text]),
                    state=[Menus.calendar, Menus.reset_complete, Menus.are_u_sure])
@dp.message_handler(Text(equals=buttons.settings_btn.text), state=[Menus.main_menu, None])
async def settings_submenu(message: Message, state: FSMContext):
    answer_text = "Вы перешли в настройки. ⚙️"
    async with state.proxy() as data:
        if message.text == buttons.edit_holidays_save_btn.text:
            await db.save_user_holidays(user_id=message.from_user.id, user_holidays=data[message.from_user.id])
            answer_text = f"Выходные обновлены. 🟢"
        elif message.text == buttons.edit_holidays_cancel_btn.text:
            answer_text = f"Последние изменения отменены. ⭕️"
        await message.answer(f"{answer_text}", reply_markup=menu.settings_submenu)
        if 'calendar_id' in data and data['calendar_id'] is not None:
            await bot.delete_message(chat_id=message.chat.id, message_id=data['calendar_id'])
            data['calendar_id'] = None
    await Menus.settings_submenu.set()
