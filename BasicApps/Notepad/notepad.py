import os
import tkinter as tk
from tkinter import ttk
from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
root = os.path.dirname(__file__)
icon_image = os.path.join(root, 'icon.ico')
Title = 'Notepad'

w = 700
h = 500

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.set_appear()

        self.show()

    def set_appear(self):
        self.resize(w, h)
        self.setWindowTitle(Title)
        self.setWindowIcon(QtGui.QIcon(icon_image))
        self.move(100, 100)

    def initUI(self):
        self.main_layout = QVBoxLayout()
        
        self.newAction = QAction('New', self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.triggered.connect(self.newFile)
        
        self.saveAction = QAction('Save', self)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.triggered.connect(self.saveFile)
        
        self.openAction = QAction('Open', self)
        self.openAction.setShortcut('Ctrl+O')
        self.openAction.triggered.connect(self.openFile)
        
        self.menubar = QMenuBar()
        self.fileMenu = self.menubar.addMenu('File')
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.openAction)

        self.txt = QTextEdit(self)
        self.main_layout.addWidget(self.menubar)
        self.main_layout.addWidget(self.txt)
        self.setLayout(self.main_layout)

    def newFile(self):
        self.txt.clear()
        self.setWindowTitle(Title)
        
    def saveFile(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt);All files (*.*)")
        if not path:
            return
        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.txt.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)
        except Exception as e:
            print(str(e))
        else:
            self.path = path
            self.setWindowTitle(path)
            self.txt.setText(text)
        
    def openFile(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);All files (*.*)")
        if path:
            try:
                with open(path, newline='') as f:
                    text = f.read()
            except Exception as e:
                print(str(e))
            else:
                self.path = path
                self.setWindowTitle(path)
                self.txt.setText(text)

app = QApplication([])
mw = MainWin()
app.exec()