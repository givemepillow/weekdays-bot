from aiogram.dispatcher.filters.state import StatesGroup, State


class YearMonthWeekday(StatesGroup):
    Year = State()
    Month = State()
    Weekday = State()
