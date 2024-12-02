import sqlite3
from datetime import datetime
from database.db_config import DatabaseConfig

class Logger:
    def __init__(self):
        self.db = DatabaseConfig()
    
    def log_action(self, user_id: int, action: str, record_type: str, record_id: int) -> bool:
        """Log an action in the audit trail"""
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    INSERT INTO Logs (user_id, action, record_type, record_id)
                    VALUES (?, ?, ?, ?)
                    """,
                    (user_id, action, record_type, record_id)
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Logging error: {str(e)}")
            return False