from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel,
    QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import pyqtSignal

class Sidebar(QWidget):
    button_clicked = pyqtSignal(str)
    
    def __init__(self, on_button_clicked):
        super().__init__()
        self.setMaximumWidth(200)
        self.setMinimumWidth(200)
        
        # Create layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Add logo/title
        title = QLabel("RMA Manager")
        title.setStyleSheet("font-size: 18px; padding: 20px;")
        layout.addWidget(title)
        
        # Create navigation buttons
        self.create_nav_button("Dashboard", "dashboard", layout)
        self.create_nav_button("RMAs", "rmas", layout)
        self.create_nav_button("Service Orders", "service_orders", layout)
        self.create_nav_button("Contacts", "contacts", layout)
        self.create_nav_button("Reports", "reports", layout)
        
        # Add spacer
        layout.addSpacerItem(
            QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        )
        
        # Add settings button at bottom
        self.create_nav_button("Settings", "settings", layout)
        
        # Connect signal
        self.button_clicked.connect(on_button_clicked)
    
    def create_nav_button(self, text, button_id, layout):
        """Create a navigation button and add it to the layout"""
        button = QPushButton(text)
        button.setStyleSheet("""
            QPushButton {
                text-align: left;
                padding: 10px 20px;
                border: none;
                background: transparent;
            }
            QPushButton:hover {
                background: #e0e0e0;
            }
        """)
        button.clicked.connect(lambda: self.button_clicked.emit(button_id))
        layout.addWidget(button)