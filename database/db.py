import aiosqlite

DB_NAME = "database/users.db"


async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            gender TEXT,
            looking_for TEXT,
            credits INTEGER DEFAULT 10
        )
        """)

        await db.commit()


async def add_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        INSERT OR IGNORE INTO users (user_id)
        VALUES (?)
        """, (user_id,))

        await db.commit()
