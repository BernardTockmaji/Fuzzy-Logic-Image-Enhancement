import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QApplication, QFileDialog
from PyQt5.QtCore import Qt, QDir

global fileName

global app


class BrowseImagesWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton('Browse Images')
        self.text = QLabel('Welcome to our Fuzzy Image Enhancement App')

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.getFile)

    def getFile(self):
        global fileName

        fileName, _ = QFileDialog.getOpenFileName(self, 'JPG Files', QDir.rootPath(), '*.jpg')

        app.exit()


def renderGUI():
    global app
    app = QApplication([])

    widget = BrowseImagesWidget()

    widget.resize(400, 400)

    widget.show()

    app.exec()
