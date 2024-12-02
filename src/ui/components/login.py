from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QMessageBox
)
from PyQt6.QtCore import pyqtSignal

class LoginWidget(QWidget):
    login_successful = pyqtSignal()
    
    def __init__(self, on_login_success):
        super().__init__()
        self.on_login_success = on_login_success
        
        # Create layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(400, 100, 400, 100)
        
        # Add title
        title = QLabel("RMA Manager Login")
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        layout.addWidget(title)
        
        # Add username field
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)
        
        # Add password field
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)
        
        # Add login button
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)
        
        # Add spacer
        layout.addStretch()
    
    def handle_login(self):
        """Handle login button click"""
        # TODO: Implement actual authentication
        username = self.username_input.text()
        password = self.password_input.text()
        
        if username and password:  # Temporary validation
            self.on_login_success()
        else:
            QMessageBox.warning(
                self,
                "Login Failed",
                "Please enter both username and password."
            )