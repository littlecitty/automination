from PyQt5.Qtwidgets import QMainWindow, QApplicatoin
from PyQt5.uic import loadUi
import sys


class MainUI(QMainWindow):
    def __init__(self):
            super(MainUI, self).__init__()

            loadUi("test1.ui", self)


if __name__ == "__main__":
      app = QApplicatoin(sys.argv)
      ui = MainUI()
      ui.show()
      app.exec_()