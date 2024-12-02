import win32com.client
from pathlib import Path
from typing import List, Optional
from database.db_config import DatabaseConfig

class EmailManager:
    def __init__(self):
        self.db = DatabaseConfig()
        self.outlook = None
        try:
            self.outlook = win32com.client.Dispatch('Outlook.Application')
        except Exception as e:
            print(f"Failed to initialize Outlook: {e}")
    
    def send_email(
        self,
        to: str,
        subject: str,
        body: str,
        attachments: Optional[List[Path]] = None,
        record_type: str = None,
        record_id: int = None
    ) -> bool:
        """Send an email using Outlook"""
        try:
            if not self.outlook:
                return False
            
            mail = self.outlook.CreateItem(0)
            mail.To = to
            mail.Subject = subject
            mail.HTMLBody = body
            
            if attachments:
                for attachment in attachments:
                    if attachment.exists():
                        mail.Attachments.Add(str(attachment))
            
            mail.Send()
            
            # Log email
            if record_type and record_id:
                with self.db.get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO EmailLog (record_type, record_id, recipient, subject, status)
                        VALUES (?, ?, ?, ?, ?)
                    """, (record_type, record_id, to, subject, "Sent"))
                    conn.commit()
            
            return True
            
        except Exception as e:
            print(f"Failed to send email: {e}")
            return False