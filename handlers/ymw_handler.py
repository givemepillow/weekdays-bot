from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.ymw import YearMonthWeekday


@dp.message_handler(Command("start"), state=None)
async def select_year(message: types.Message):
    await message.answer("Выбирете год.")
    await YearMonthWeekday.Year()


@dp.message_handler(state=YearMonthWeekday.Year)
async def select_month(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year'] = message.text
    await message.answer("Выберите месяц.")
    await YearMonthWeekday.Month()


@dp.message_handler(state=YearMonthWeekday.Month)
async def select_weekday(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['month'] = message.text
    await YearMonthWeekday.Weekday()
