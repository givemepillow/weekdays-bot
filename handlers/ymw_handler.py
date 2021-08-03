import calendar
import datetime

import numpy as np
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.ymw import YearMonthWeekday

current_year = datetime.datetime.now().year
years = [current_year - 1, current_year, current_year + 1]

months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
          'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']


@dp.message_handler(Command("cancel"), state=None)
async def cancel():
    pass


@dp.message_handler(Command("cancel"), state="*")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Отмена.", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(Command("start"), state=None)
async def select_year(message: types.Message):
    global years
    buttons = [str(year) for year in years]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)
    await message.answer("Выбирете год.", reply_markup=keyboard)
    await YearMonthWeekday.first()


@dp.message_handler(state=YearMonthWeekday.Year)
async def select_month(message: types.Message, state: FSMContext):
    global years
    if message.text not in (str(y) for y in years):
        await message.answer("Выбирете год из доступных!")
        await YearMonthWeekday.first()
    else:
        async with state.proxy() as data:
            data['year'] = int(message.text)
        global months
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*months)
        await message.answer("Выберите месяц.", reply_markup=keyboard)
        await YearMonthWeekday.next()


@dp.message_handler(state=YearMonthWeekday.Month)
async def select_weekday(message: types.Message, state: FSMContext):
    global months
    if message.text not in months:
        await message.answer("Выберите месяц из списка!")
        await YearMonthWeekday.first()
        await YearMonthWeekday.next()
    else:
        async with state.proxy() as data:
            data['month'] = months.index(message.text) + 1
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*weekdays)
        await message.answer("Выберите день недели.", reply_markup=keyboard)
        await YearMonthWeekday.next()


@dp.message_handler(state=YearMonthWeekday.Weekday)
async def days_of_week_in_month(message: types.Message, state: FSMContext):
    global weekdays
    if message.text not in weekdays:
        await message.answer("Выберите день недели из списка!")
    else:
        async with state.proxy() as data:
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            year = data['year']
            month = data['month']
            start_day, end_day = 1, calendar.monthrange(data['year'], data['month'])[1]
            count_of_days = np.busday_count(f"{year}-{month:02}",
                                            f"{year}-{((month + 1) % 13):02}",
                                            weekmask=f"{days[weekdays.index(message.text)]}")
            await message.answer(f"В с {start_day:02}.{month:02}.{year} по "
                                 f"{end_day:02}.{month:02}.{year} "
                                 f" {count_of_days} {message.text.lower()}.",
                                 reply_markup=types.ReplyKeyboardRemove())
        await state.finish()
