import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(500, 300, 450, 500)
        self.setWindowTitle('Управление НЛО')
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.label.setText("")
        self.pixmap = QPixmap('nlo.jpg')
        self.label.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            if self.label.x() - 25 > 0:
                self.label.setGeometry(QtCore.QRect(self.label.x() - 25, self.label.y(), 50, 50))
            else:
                self.label.setGeometry(QtCore.QRect(400, self.label.y(), 50, 50))
        elif event.key() == Qt.Key_Right:
            if self.label.x() + 25 < 425:
                self.label.setGeometry(QtCore.QRect(self.label.x() + 25, self.label.y(), 50, 50))
            else:
                self.label.setGeometry(QtCore.QRect(0, self.label.y(), 50, 50))
        elif event.key() == Qt.Key_Up:
            if 0 < self.label.y() - 25:
                self.label.setGeometry(QtCore.QRect(self.label.x(), self.label.y() - 25, 50, 50))
            else:
                self.label.setGeometry(QtCore.QRect(self.label.x(), 450, 50, 50))
        elif event.key() == Qt.Key_Down:
            if self.label.y() + 25 < 475:
                self.label.setGeometry(QtCore.QRect(self.label.x(), self.label.y() + 25, 50, 50))
            else:
                self.label.setGeometry(QtCore.QRect(self.label.x(), 0, 50, 50))
        self.label.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())