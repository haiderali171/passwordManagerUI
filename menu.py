import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

class Window2(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Store Your Password Here')


class LoginForm(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Password Manager')
		self.resize(600, 400)

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your username')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		label_email = QLabel('<font size="4"> Email Add </font>')
		self.lineEdit_email = QLineEdit()
		self.lineEdit_email.setPlaceholderText('Please enter your email address here')
		layout.addWidget(label_email, 2, 0)
		layout.addWidget(self.lineEdit_email, 2, 1)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 3, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		button_login_signed = QPushButton('Already Signed UP? Click here')
		button_login_signed.clicked.connect(self.show_window2)
		layout.addWidget(button_login_signed, 4, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()

		if self.lineEdit_username.text() == 'Usernmae' and self.lineEdit_password.text() == '000':
			msg.setText('Success')
			msg.exec_()
			app.quit()
		else:
			msg.setText('Incorrect Password')
			msg.exec_()

	def show_window2(self):
		self.window = Window2()
		self.window.show()
		self.hide()

if __name__ == '__main__':
	app = QApplication(sys.argv)

	form = LoginForm()
	form.show()

	sys.exit(app.exec_())