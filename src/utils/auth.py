import bcrypt
import sqlite3
from database.db_config import DatabaseConfig

class AuthManager:
    def __init__(self):
        self.db = DatabaseConfig()
    
    def hash_password(self, password: str) -> str:
        """Hash a password using bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify a password against its hash"""
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    
    def authenticate_user(self, username: str, password: str) -> tuple[bool, str, dict]:
        """Authenticate a user and return (success, message, user_data)"""
        try:
            with self.db.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT user_id, password_hash, role FROM Users WHERE username = ? AND is_active = 1",
                    (username,)
                )
                result = cursor.fetchone()
                
                if not result:
                    return False, "Invalid username or password", {}
                
                user_id, stored_hash, role = result
                
                if not self.verify_password(password, stored_hash):
                    return False, "Invalid username or password", {}
                
                # Update last login timestamp
                cursor.execute(
                    "UPDATE Users SET last_login = CURRENT_TIMESTAMP WHERE user_id = ?",
                    (user_id,)
                )
                conn.commit()
                
                return True, "Login successful", {
                    "user_id": user_id,
                    "username": username,
                    "role": role
                }
                
        except Exception as e:
            return False, f"Authentication error: {str(e)}", {}