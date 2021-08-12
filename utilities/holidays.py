from datetime import datetime

from loader import db
from .date_names import months_names


async def holidays(user_id):
    data = {}
    days = sorted(await db.get_user_holidays(user_id))
    for day in days:
        monthname = months_names[datetime.fromtimestamp(day).month - 1]
        monthname += f" {datetime.fromtimestamp(day).year}"
        if monthname not in data:
            data[monthname] = []
        data[monthname].append(datetime.fromtimestamp(day).day)

    return data
