from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.ymw import YearMonthWeekday


@dp.message_handler(Command("start"), state=None)
async def select_year(message: types.Message):
    await message.answer("Выбирете год.")
    await YearMonthWeekday.first()


@dp.message_handler(state=YearMonthWeekday.Year)
async def select_month(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['year'] = message.text
    await message.answer("Выберите месяц.")
    await YearMonthWeekday.next()


@dp.message_handler(state=YearMonthWeekday.Month)
async def select_weekday(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['month'] = message.text
    await message.answer("Выберите день.")
    await YearMonthWeekday.next()


@dp.message_handler(state=YearMonthWeekday.Weekday)
async def days_of_week_in_month(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(f"Вы выбрали {data['year']} год, "
                             f"{data['month']}  и {message.text} день.")
    await state.finish()
