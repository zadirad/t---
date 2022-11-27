import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QStatusBar
from PyQt5 import uic


class QMainWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('anti.ui', self)
        self.MainWindow()

    def MainWindow(self):
        self.statusBar = QStatusBar(self)
        self.statusBar.resize(400, 25)
        self.statusBar.move(100, 525)
        self.res_Button.clicked.connect(self.run)

    def run(self):
        self.text1 = self.Text1.toPlainText().split("\n")
        self.text2 = self.Text2.toPlainText().split("\n")
        self.text1 = [i for i in self.text1 if i != '']
        self.text2 = [i for i in self.text2 if i != '']
        if len(self.text2) >= len(self.text1):
            z = len(self.text2)
        else:
            z = len(self.text1)

        c = 0
        for i in range(z):
            if i < len(self.text1) and i < len(self.text2):
                if self.text1[i] == self.text2[i]:
                    c += 1
        if z == 0:
            per = 100
        else:
            per = round(c / z, 4) * 100
        self.statusBar.showMessage("Коды похожи на " + str(per) + "%")
        if per > self.porog.value():
            self.statusBar.setStyleSheet("background-color: red")
        else:
            self.statusBar.setStyleSheet("background-color: green")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QMainWindow()
    ex.show()
    sys.exit(app.exec())