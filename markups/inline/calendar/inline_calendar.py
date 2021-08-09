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

storage = []

calendar_cb = CallbackData(CALLBACKDATA_ID, ACTION, YEAR, MONTH, DAY)

class InlineCalendar:
    weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    CHECK_MARK = '✅'

    def __init__(self):
        locale.setlocale(locale.LC_ALL, "ru_RU")

    async def __call__(self,
                       year: int = datetime.now().year,
                       month: int = datetime.now().month,
                       day: int = datetime.now().day
                       ) -> InlineKeyboardMarkup:

        inline_kb = InlineKeyboardMarkup(row_width=7)
        plug_cb = calendar_cb.new(PLUG, year, month, day)

        # Row with year.
        inline_kb.row()
        inline_kb.insert(InlineKeyboardButton(
            "<<",
            callback_data=calendar_cb.new(PREV_YEAR, year, month, day)
        ))

        inline_kb.insert(InlineKeyboardButton(
            f'{str(year)}',
            callback_data=plug_cb
        ))

        inline_kb.insert(InlineKeyboardButton(
            ">>",
            callback_data=calendar_cb.new(NEXT_YEAR, year, month, day)
        ))

        # Row with month.
        inline_kb.row()
        inline_kb.insert(InlineKeyboardButton(
            "<", callback_data=calendar_cb.new(PREV_MONTH, year, month, day)
        ))

        inline_kb.insert(InlineKeyboardButton(
            f'{calendar.month_name[month]}',
            callback_data=plug_cb
        ))

        inline_kb.insert(InlineKeyboardButton(
            ">", callback_data=calendar_cb.new(NEXT_MONTH, year, month, day)
        ))

        # Row with week days.
        inline_kb.row()
        for weekday in self.weekdays:
            inline_kb.insert(InlineKeyboardButton(weekday, callback_data=plug_cb))

        # Rows with days.
        month_calendar = calendar.monthcalendar(year, month)
        for week in month_calendar:
            inline_kb.row()
            for day in week:
                if day == 0:
                    inline_kb.insert(InlineKeyboardButton(" ", callback_data=plug_cb))
                else:
                    if int(datetime(int(year), int(month), int(day)).timestamp()) in storage:

                        inline_kb.insert(InlineKeyboardButton(
                            self.CHECK_MARK, callback_data=calendar_cb.new(TARGET_DATE, year, month, day)
                        ))
                    else:
                        inline_kb.insert(InlineKeyboardButton(
                            str(day), callback_data=calendar_cb.new(TARGET_DATE, year, month, day)
                        ))

        return inline_kb


    async def selection(self, query: CallbackQuery, data: CallbackData) -> tuple[bool, datetime]:
        selected, date = False, None
        temp_date = datetime(int(data[YEAR]), int(data[MONTH]), 1)
