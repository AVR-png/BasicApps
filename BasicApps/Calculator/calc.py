import os
import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from functools import partial
root = os.path.dirname(__file__)
icon_image = os.path.join(root, 'icon.ico')

WINDOW_SIZE = 240
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

operator = " "


class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.btnclicked()

        self.show()

    def set_appear(self):
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.setWindowIcon(QIcon(icon_image))
        self.setWindowTitle('Calculator')
        self.move(100, 100)


    def initUI(self):
        self.MainLayout = QVBoxLayout()
        self.Widget = QWidget(self)
        self.Widget.setLayout(self.MainLayout)

        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.MainLayout.addWidget(self.display)

    #def createButtons(self):
        self.btnMap = {}
        btnLayout = QGridLayout()
        keyBoard = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.btnMap[key] = QPushButton(key)
                self.btnMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                btnLayout.addWidget(self.btnMap[key], row, col)

        self.MainLayout.addLayout(btnLayout)


    def setDisplayText(self, text):
        """Set the display's text."""
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        """Get the display's text."""
        return self.display.text()


    def clear(self):
        global operator
        operator = ''
        self.setDisplayText("")

    def answer(self):
        global operator
        try:
            result = str(eval(operator))
        except Exception:
            result = 'ERROR'
        self.display.setText(result)
        operator = result

    def input(self, num):
        global operator
        operator = operator + str(num)
        self.display.setText(operator)
        

    def btnclicked(self):
        for key, button in self.btnMap.items():
            if key not in {"=", "C"}:
                button.clicked.connect(
                    partial(self.input, key)
                )
        self.btnMap["="].clicked.connect(self.answer)
        self.btnMap["C"].clicked.connect(self.clear)

    def keyPressEvent(self, event):
        if isinstance(event, QKeyEvent):
            key_text = event.text()
            if event.key() == Qt.Key.Key_Enter or event.key() == Qt.Key.Key_Return:
                self.answer()
            elif event.key() == Qt.Key.Key_C or event.key() == Qt.Key.Key_Delete:
                self.clear()
            for key, button in self.btnMap.items():
                if key_text == key and key_text != '=':
                    self.input(key_text)
                
    
app = QApplication([])
mw = Calc()
app.exec()