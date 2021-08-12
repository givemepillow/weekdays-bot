import calendar
from datetime import date, timedelta, datetime

from loader import db

months_names = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                'Ноябрь', 'Декабрь']


async def count_weekdays(user_id: int, start_date=date(datetime.now().year, 9, 1),
                         end_date=date(datetime.now().year + 1, 5, 31)):
    weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    holidays = await db.get_user_holidays(user_id)
    result = {}
    for w in weekdays:
        result[w] = 0
    delta = timedelta(days=1)
    start = start_date
    end = end_date
    while start <= end:
        if int(datetime(int(start.year), int(start.month), int(start.day)).timestamp()) not in holidays:
            result[weekdays[start.weekday()]] += 1
        start += delta
    return result


async def count_weekdays_by_month(user_id: int):
    weekdays = {}
    start = date(datetime.now().year, 9, 1)
    end = date(datetime.now().year + 1, 5, 31)
    while start <= end:
        monthname = months_names[start.month - 1]
        month_weekdays = await count_weekdays(user_id,
                                              date(start.year, start.month, 1),
                                              date(start.year, start.month,
                                                   calendar.monthrange(start.year, start.month)[1]))
        weekdays[monthname] = month_weekdays
        start += timedelta(days=31)
    return weekdays
