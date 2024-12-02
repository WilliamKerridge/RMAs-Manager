from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStackedWidget
)
from PyQt6.QtCore import Qt
from .components.sidebar import Sidebar
from .components.dashboard import Dashboard
from .components.login import LoginWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RMA Manager")
        self.setMinimumSize(1200, 800)
        
        # Initialize the central widget and main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        
        # Initialize stacked widget for main content
        self.stacked_widget = QStackedWidget()
        
        # Create and add login widget
        self.login_widget = LoginWidget(self.on_login_success)
        self.stacked_widget.addWidget(self.login_widget)
        
        # Create main application layout (sidebar + content)
        self.app_widget = QWidget()
        self.app_layout = QHBoxLayout(self.app_widget)
        
        # Create sidebar
        self.sidebar = Sidebar(self.on_sidebar_button_clicked)
        self.app_layout.addWidget(self.sidebar)
        
        # Create dashboard
        self.dashboard = Dashboard()
        self.app_layout.addWidget(self.dashboard)
        
        # Add app widget to stacked widget
        self.stacked_widget.addWidget(self.app_widget)
        
        # Add stacked widget to main layout
        self.main_layout.addWidget(self.stacked_widget)
        
        # Start with login widget
        self.stacked_widget.setCurrentWidget(self.login_widget)
    
    def on_login_success(self):
        """Handle successful login"""
        self.stacked_widget.setCurrentWidget(self.app_widget)
    
    def on_sidebar_button_clicked(self, button_id):
        """Handle sidebar button clicks"""
        # TODO: Implement navigation logic
        pass