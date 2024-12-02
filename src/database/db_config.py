import sqlite3
import os
from pathlib import Path

class DatabaseConfig:
    def __init__(self):
        self.db_path = Path('data/rma_manager.db')
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
    def get_connection(self):
        """Create and return a database connection"""
        return sqlite3.connect(str(self.db_path))
        
    def initialize_database(self):
        """Initialize the database with all required tables"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Create Users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL,
                    role TEXT NOT NULL,
                    email TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP,
                    is_active BOOLEAN DEFAULT 1
                )
            ''')
            
            # Create RMA table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS RMA (
                    rma_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    rma_number TEXT NOT NULL UNIQUE,
                    company_id INTEGER NOT NULL,
                    contact_id INTEGER,
                    product_name TEXT NOT NULL,
                    issue_description TEXT,
                    status TEXT NOT NULL,
                    priority TEXT,
                    date_created DATE DEFAULT CURRENT_DATE,
                    last_updated DATE DEFAULT CURRENT_DATE,
                    attachment_id INTEGER,
                    FOREIGN KEY (company_id) REFERENCES CompanyContacts (company_id),
                    FOREIGN KEY (contact_id) REFERENCES ContactDetails (contact_id),
                    FOREIGN KEY (attachment_id) REFERENCES Attachments (attachment_id)
                )
            ''')
            
            # Create ServiceOrders table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ServiceOrders (
                    service_order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    rma_id INTEGER,
                    company_id INTEGER NOT NULL,
                    contact_id INTEGER,
                    product_name TEXT NOT NULL,
                    service_description TEXT,
                    status TEXT NOT NULL,
                    priority TEXT,
                    days_open INTEGER DEFAULT 0,
                    date_created DATE DEFAULT CURRENT_DATE,
                    last_updated DATE DEFAULT CURRENT_DATE,
                    attachment_id INTEGER,
                    FOREIGN KEY (rma_id) REFERENCES RMA (rma_id),
                    FOREIGN KEY (company_id) REFERENCES CompanyContacts (company_id),
                    FOREIGN KEY (contact_id) REFERENCES ContactDetails (contact_id),
                    FOREIGN KEY (attachment_id) REFERENCES Attachments (attachment_id)
                )
            ''')
            
            # Create CompanyContacts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS CompanyContacts (
                    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_name TEXT NOT NULL UNIQUE,
                    address TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT 1
                )
            ''')
            
            # Create ContactDetails table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ContactDetails (
                    contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    company_id INTEGER NOT NULL,
                    contact_name TEXT NOT NULL,
                    email TEXT,
                    phone TEXT,
                    role TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT 1,
                    FOREIGN KEY (company_id) REFERENCES CompanyContacts (company_id)
                )
            ''')
            
            # Create Attachments table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Attachments (
                    attachment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    record_type TEXT NOT NULL,
                    record_id INTEGER NOT NULL,
                    file_name TEXT NOT NULL,
                    file_path TEXT NOT NULL,
                    uploaded_by INTEGER,
                    upload_date DATE DEFAULT CURRENT_DATE,
                    FOREIGN KEY (uploaded_by) REFERENCES Users (user_id)
                )
            ''')
            
            # Create Logs table for audit trail
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Logs (
                    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    action TEXT NOT NULL,
                    record_type TEXT NOT NULL,
                    record_id INTEGER,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES Users (user_id)
                )
            ''')
            
            # Create EmailLog table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS EmailLog (
                    email_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    record_type TEXT NOT NULL,
                    record_id INTEGER NOT NULL,
                    recipient TEXT NOT NULL,
                    subject TEXT NOT NULL,
                    status TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()