import calendar
import locale
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types import CallbackQuery

PREV_YEAR = 'PREV-YEAR'
NEXT_YEAR = 'NEXT-YEAR'
PREV_MONTH = 'PREV-MONTH'
NEXT_MONTH = 'NEXT-MONTH'
TARGET_DATE = 'TARGET-DATE'
PLUG = 'PLUG'
ACTION = 'ACTION'
YEAR, MONTH, DAY = 'YEAR', 'MONTH', 'DAY'
CALLBACKDATA_ID = 'CALENDAR'

calendar_cb = CallbackData(CALLBACKDATA_ID, ACTION, YEAR, MONTH, DAY)

class InlineCalendar:
    weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

    def __init__(self):
        locale.setlocale(locale.LC_ALL, "ru_RU")

    async def __call__(self,
                       year: int = datetime.now().year,
                       month: int = datetime.now().month,
                       day: int = datetime.now().day
                       ) -> InlineKeyboardMarkup:

        inline_kb = InlineKeyboardMarkup(row_width=7)
        plug_cb = calendar_cb.new(PLUG, year, month, day)
