import sys
import logging
from PySide6.QtWidgets import QApplication
from src.app.core.logging import setup_logging
from src.app.ui.main_window import MainWindow

logger = logging.getLogger(__name__)

def main() -> int:
    setup_logging()
    logger.info("Starting application...")

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    raise SystemExit(main())
