import os
import sys
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
root = os.path.dirname(__file__)
icon_image = os.path.join(root, 'icon.ico')

w = 300
h = 150

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()

    def set_appear(self):
        self.setFixedSize(w, h)
        self.setWindowIcon(QIcon(icon_image))
        self.setWindowTitle('Clock')
        self.move(100, 100)

    def initUI(self):
        self.mainlayout = QVBoxLayout()
        
        self.time = QLabel()
        self.time.setAlignment(Qt.AlignCenter)
        font = QFont('Arial', 50, QFont.Bold)
        self.time.setFont(font)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.timeout.connect(self.showDate)
        self.timer.start(1000)

        self.date = QLabel()
        self.date.setAlignment(Qt.AlignCenter)
        font2 = QFont('Arial', 20, QFont.Bold)
        self.date.setFont(font2)

        self.mainlayout.addWidget(self.time)
        self.mainlayout.addWidget(self.date)
        self.setLayout(self.mainlayout)

    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.time.setText(label_time)

    def showDate(self):
        label_date = datetime.date.today()
        self.date.setText(str(label_date))

app = QApplication([])
mw = Clock()
app.exec()
