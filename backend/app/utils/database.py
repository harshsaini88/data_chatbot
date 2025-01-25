import sqlite3
from contextlib import contextmanager

class DatabaseManager:
    def __init__(self, db_path='memory_chatbot.db'):
        self.db_path = db_path
        self._create_tables()

    def _create_tables(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY,
                    user_message TEXT,
                    ai_response TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()

    @contextmanager
    def _get_connection(self):
        conn = sqlite3.connect(self.db_path)
        try:
            yield conn
        finally:
            conn.close()

    def log_interaction(self, user_message: str, ai_response: str):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO interactions (user_message, ai_response) 
                VALUES (?, ?)
            ''', (user_message, ai_response))
            conn.commit()