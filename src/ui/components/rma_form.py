from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QTextEdit, QComboBox, QPushButton, QMessageBox
)
from repositories.rma_repository import RMARepository

class RMAForm(QWidget):
    def __init__(self, rma_id: int = None):
        super().__init__()
        self.rma_id = rma_id
        self.rma_repo = RMARepository()
        
        # Create layout
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # Create form fields
        self.product_name = QLineEdit()
        self.issue_description = QTextEdit()
        self.status = QComboBox()
        self.status.addItems(["Open", "Pending", "Closed"])
        self.priority = QComboBox()
        self.priority.addItems(["High", "Medium", "Low"])
        
        # Add fields to form layout
        form_layout.addRow("Product Name:", self.product_name)
        form_layout.addRow("Issue Description:", self.issue_description)
        form_layout.addRow("Status:", self.status)
        form_layout.addRow("Priority:", self.priority)
        
        # Add form layout to main layout
        layout.addLayout(form_layout)
        
        # Add save button
        save_button = QPushButton("Save RMA")
        save_button.clicked.connect(self.save_rma)
        layout.addWidget(save_button)
        
        # Load data if editing existing RMA
        if self.rma_id:
            self.load_rma_data()
    
    def load_rma_data(self):
        """Load existing RMA data into form"""
        rma_data = self.rma_repo.get_rma_by_id(self.rma_id)
        if rma_data:
            self.product_name.setText(rma_data['product_name'])
            self.issue_description.setText(rma_data['issue_description'])
            self.status.setCurrentText(rma_data['status'])
            self.priority.setCurrentText(rma_data['priority'])
    
    def save_rma(self):
        """Save RMA data"""
        data = {
            'product_name': self.product_name.text(),
            'issue_description': self.issue_description.toPlainText(),
            'status': self.status.currentText(),
            'priority': self.priority.currentText()
        }
        
        if self.rma_id:
            success, message = self.rma_repo.update_rma(self.rma_id, data)
        else:
            success, _, message = self.rma_repo.create_rma(data)
        
        if success:
            QMessageBox.information(self, "Success", message)
        else:
            QMessageBox.warning(self, "Error", message)