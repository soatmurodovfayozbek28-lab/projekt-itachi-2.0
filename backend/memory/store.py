import sqlite3
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(__file__).resolve().parents[2]
DB_DIR = BASE_DIR / "database"
DB_PATH = DB_DIR / "itachi.db"


class MemoryStore:

    def __init__(self):
        DB_DIR.mkdir(parents=True, exist_ok=True)
        self.create_table()

    def connect(self):
        return sqlite3.connect(DB_PATH)

    def create_table(self):
        with self.connect() as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)

    def save(self, category, content):
        with self.connect() as db:
            db.execute(
                """INSERT INTO memories
                (category, content, created_at)
                VALUES (?, ?, ?)""",
                (category, content, datetime.now().isoformat())
            )

        return {"status": "saved"}

    def get_recent(self, limit=20):
        with self.connect() as db:
            rows = db.execute(
                """SELECT id, category, content, created_at
                FROM memories
                ORDER BY id DESC LIMIT ?""",
                (limit,)
            ).fetchall()

        return rows

    def search(self, keyword):
        with self.connect() as db:
            rows = db.execute(
                """SELECT id, category, content, created_at
                FROM memories
                WHERE content LIKE ?
                ORDER BY id DESC""",
                (f"%{keyword}%",)
            ).fetchall()

        return rows


memory = MemoryStore()