# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QMainWindow, QAction


class MainWindow(QMainWindow):
    def __init__(self,widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Ford-SEU GLOSA Demo")
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        self.control_menu = self.menu.addMenu("Control")
        self.about_menu = self.menu.addMenu("About")

        # Connect QAction
        connect_action = QAction("Connect SOCKET", self)


        # Disconnect QAction
        disconnect_action = QAction("Disconnect SOCKET", self)


        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(connect_action)
        self.file_menu.addAction(disconnect_action)
        self.file_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")

        # Window dimensions
        geometry = QtCore.qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.8, geometry.height() * 0.7)

        self.setCentralWidget(widget)
