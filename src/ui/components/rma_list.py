from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QLabel, QComboBox
)
from PyQt6.QtCore import Qt

class RMAList(QWidget):
    def __init__(self):
        super().__init__()
        
        # Create main layout
        layout = QVBoxLayout(self)
        
        # Create header with title and controls
        header_layout = QHBoxLayout()
        
        # Add title
        title = QLabel("RMA List")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        header_layout.addWidget(title)
        
        # Add filter dropdown
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["All", "Open", "Closed", "Pending"])
        header_layout.addWidget(self.filter_combo)
        
        # Add new RMA button
        new_button = QPushButton("New RMA")
        new_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        header_layout.addWidget(new_button)
        
        # Add header layout to main layout
        layout.addLayout(header_layout)
        
        # Create table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "RMA Number", "Company", "Product", "Status",
            "Priority", "Date Created"
        ])
        
        # Set table properties
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        # Add table to layout
        layout.addWidget(self.table)
        
        # Load initial data
        self.load_data()
    
    def load_data(self):
        """Load RMA data into the table"""
        # TODO: Implement actual data loading from database
        # This is temporary sample data
        sample_data = [
            ("RMA001", "Company A", "Product X", "Open", "High", "2024-01-15"),
            ("RMA002", "Company B", "Product Y", "Pending", "Medium", "2024-01-14"),
            ("RMA003", "Company C", "Product Z", "Closed", "Low", "2024-01-13"),
        ]
        
        self.table.setRowCount(len(sample_data))
        
        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, col, item)
        
        # Adjust column widths
        self.table.resizeColumnsToContents()