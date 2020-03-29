# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2.QtGui import QKeySequence
from PySide2.QtWidgets import QMainWindow, QAction
import dialog


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


        # Record QAction
        start_record_action = QAction("Start Record",self)
        # start_record_action.triggered.connect()

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)

        # About QAction
        about_action = QAction("About", self)
        exit_action.triggered.connect(dialog.about)

        self.file_menu.addAction(connect_action)
        self.file_menu.addAction(disconnect_action)
        self.file_menu.addAction(exit_action)
        self.control_menu.addAction(start_record_action)
        self.about_menu.addAction(about_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Data loaded and plotted")

        # Window dimensions
        geometry = QtCore.qApp.desktop().availableGeometry(self)
        self.setFixedSize(geometry.width() * 0.65, geometry.height() * 0.6)

        self.setCentralWidget(widget)
