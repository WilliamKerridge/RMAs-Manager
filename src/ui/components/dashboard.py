from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QFrame
)
from PyQt6.QtCore import Qt

class DashboardWidget(QFrame):
    def __init__(self, title, value):
        super().__init__()
        self.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        self.setStyleSheet("""
            QFrame {
                background: white;
                border-radius: 8px;
                padding: 15px;
            }
        """)
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Add title
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 14px; color: #666;")
        layout.addWidget(title_label)
        
        # Add value
        value_label = QLabel(str(value))
        value_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(value_label)

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create main layout
        layout = QVBoxLayout(self)
        
        # Add title
        title = QLabel("Dashboard")
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Create widgets layout
        widgets_layout = QHBoxLayout()
        
        # Add dashboard widgets
        widgets_layout.addWidget(DashboardWidget("Open RMAs", "12"))
        widgets_layout.addWidget(DashboardWidget("Pending Service Orders", "8"))
        widgets_layout.addWidget(DashboardWidget("Overdue Repairs", "3"))
        
        # Add widgets layout to main layout
        layout.addLayout(widgets_layout)
        
        # Add spacer
        layout.addStretch()