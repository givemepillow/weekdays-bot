from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from states.ymw import YearMonthWeekday


@dp.message_handler(Command("start"), state=None)
async def select_year(message: types.Message):
    await message.answer("Выбирете год.")
    await YearMonthWeekday.first()
