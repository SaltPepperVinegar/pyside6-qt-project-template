from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtGui import QAction
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My PySide6 App")
        self.resize(900, 600)

        label = QLabel("Hello PySide6 👋")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        self._build_menu()

    def _build_menu(self) -> None:
        menubar = self.menuBar()
 
        file_menu = menubar.addMenu("&File")
        action_quit = QAction("Quit", self)
        action_quit.triggered.connect(self.close)
        file_menu.addAction(action_quit)

        help_menu = menubar.addMenu("&Help")
        action_about = QAction("About", self)
        action_about.triggered.connect(self._about)
        help_menu.addAction(action_about)

    def _about(self) -> None:
        self.statusBar().showMessage("My PySide6 App — ready for production structure.", 5000)
