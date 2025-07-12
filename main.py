import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QProgressBar
from PyQt5.QtGui import QFont

class PasswordChecker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Strength Checker")
        self.setGeometry(100, 100, 400, 200)
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Enter your password:")
        self.label.setFont(QFont("Arial", 14))
        layout.addWidget(self.label)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.textChanged.connect(self.check_password_strength)
        layout.addWidget(self.password_input)

        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 11))
        layout.addWidget(self.result_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def check_password_strength(self):
        password = self.password_input.text()
        score = 0
        rules = []

        if len(password) >= 8:
            score += 1
        else:
            rules.append("At least 8 characters long")
        if re.search(r"[A-Z]", password):
            score += 1
        else:
            rules.append("At least one uppercase letter")
        if re.search(r"[a-z]", password):
            score += 1
        else:
            rules.append("At least one lowercase letter")
        if re.search(r"[0-9]", password):
            score += 1
        else:
            rules.append("At least one number")
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
        else:
            rules.append("At least one special character")

        self.progress_bar.setValue(score * 20)
        if score == 5:
            self.result_label.setText("Strong password")
            self.result_label.setStyleSheet("color: green;")
        elif score >= 3:
            self.result_label.setText("Moderate password")
            self.result_label.setStyleSheet("color: orange;")
        else:
            self.result_label.setText("Weak password")
            self.result_label.setStyleSheet("color: red;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    checker =  PasswordChecker()
    checker.show()
    sys.exit(app.exec_())