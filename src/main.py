import sys
from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from database.db_config import DatabaseConfig

def main():
    # Initialize database
    db = DatabaseConfig()
    db.initialize_database()
    
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Start the event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()