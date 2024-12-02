import os
from pathlib import Path

class Config:
    # Application paths
    BASE_DIR = Path(__file__).parent.parent.parent
    DATA_DIR = BASE_DIR / "data"
    ATTACHMENTS_DIR = DATA_DIR / "attachments"
    
    # Database
    DATABASE_PATH = DATA_DIR / "rma_manager.db"
    
    # Create necessary directories
    DATA_DIR.mkdir(exist_ok=True)
    ATTACHMENTS_DIR.mkdir(exist_ok=True)
    
    # Application settings
    MAX_ATTACHMENT_SIZE = 10 * 1024 * 1024  # 10MB
    ALLOWED_EXTENSIONS = {'.pdf', '.jpg', '.jpeg', '.png', '.xlsx', '.docx', '.txt'}
    
    @staticmethod
    def is_valid_file_extension(filename: str) -> bool:
        return Path(filename).suffix.lower() in Config.ALLOWED_EXTENSIONS