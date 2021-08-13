import json

import aiosqlite


class Database:
    def __init__(self, db_name, table_name="users_holidays"):
        self.db_name = db_name
        self.table_name = table_name
        self.connection = None

    async def is_user_exists(self, user_id):
        user = await self.connection.execute_fetchall(f"SELECT COUNT(*) FROM {self.table_name} WHERE user_id = ?;",
                                                      (user_id,)
                                                      )
        return False if user[0][0] == 0 else True

    async def create(self):
        self.connection = await aiosqlite.connect(self.db_name)
        await self.connection.execute(f"CREATE TABLE IF NOT EXISTS {self.table_name} ("
                                      "user_id INTEGER PRIMARY KEY,"
                                      "holidays TEXT"
                                      ");")
        await self.connection.commit()

    async def save_user_holidays(self, user_id: int, user_holidays: dict):
        if not await self.is_user_exists(user_id):
            await self.connection.execute(
                f"INSERT INTO {self.table_name} (user_id, holidays) VALUES (?, ?);",
                (user_id, str(json.dumps(user_holidays)))
            )
            assert self.connection.total_changes > 0
        else:
            await self.connection.execute(
                f"UPDATE {self.table_name} SET holidays = ? WHERE user_id = ?",
                (str(json.dumps(user_holidays)), user_id)
            )
        await self.connection.commit()

    async def get_user_holidays(self, user_id: int):
        async with aiosqlite.connect(self.db_name) as db:
            if await self.is_user_exists(user_id):
                holidays = await db.execute_fetchall(
                    f"SELECT holidays FROM {self.table_name} WHERE user_id = ?;",
                    (user_id,)
                )
                return json.loads(holidays[0][0])
            else:
                return []

    async def close(self):
        await self.connection.close()
