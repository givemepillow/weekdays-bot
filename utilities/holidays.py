from datetime import datetime
import calendar
from loader import db


async def holidays(user_id):
    data = {}
    days = sorted(await db.get_user_holidays(user_id))
    for day in days:
        monthname = calendar.month_name[datetime.fromtimestamp(day).month]
        monthname += f" {datetime.fromtimestamp(day).year}"
        if monthname not in data:
            data[monthname] = []
        data[monthname].append(datetime.fromtimestamp(day).day)

    return data
