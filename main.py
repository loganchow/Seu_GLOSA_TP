# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication
from MainWindow import MainWindow
from Widget import Widget

if __name__ == "__main__":
    app = QApplication([])

    widget = Widget()

    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec_())
