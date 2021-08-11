import json

import aiosqlite


class Database:
    def __init__(self, db_name, table_name="users_holidays"):
        self.db_name = db_name
        self.table_name = table_name

    async def is_user_exists(self, user_id):
        async with aiosqlite.connect(self.db_name) as db:
            user = await db.execute_fetchall(f"SELECT COUNT(*) FROM {self.table_name} WHERE user_id = {user_id};")
            return False if user[0][0] == 0 else True

    async def create(self):
        async with aiosqlite.connect(self.db_name) as db:
            await db.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
                             "user_id INTEGER PRIMARY KEY,"
                             "holidays TEXT"
                             ");")
            await db.commit()

    async def save_user_holidays(self, user_id: int, user_holidays: dict):
        async with aiosqlite.connect(self.db_name) as db:
            if not await self.is_user_exists(user_id):
                await db.execute(
                    f"INSERT INTO {self.table_name} (user_id, holidays) VALUES (?, ?);",
                    (user_id, str(json.dumps(user_holidays))))
                assert db.total_changes > 0
            else:
                await db.execute(
                    f"UPDATE {self.table_name} SET holidays = ? WHERE user_id = ?",
                    (str(json.dumps(user_holidays)), user_id))
            await db.commit()

    async def get_user_holidays(self, user_id: int):
        async with aiosqlite.connect(self.db_name) as db:
            if await self.is_user_exists(user_id):
                holidays = await db.execute_fetchall(
                    f"SELECT holidays FROM {self.table_name} WHERE user_id = {user_id};")
                return json.loads(holidays[0][0])
            else:
                return []
