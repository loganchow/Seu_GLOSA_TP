# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets

class about(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("About")
        self.content = QtWidgets.QLabel(self,"Developed by Logan Zhou.")
        self.show()
    # Run the main Qt loop
    # sys.exit(app.exec_())


