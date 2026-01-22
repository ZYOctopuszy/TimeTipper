if __name__ == "__main__":
    from main_class import MainWindow

from PySide6.QtWidgets import QComboBox
from datetime import datetime


class DayManager:
    def __init__(self, p_window: MainWindow, day_widget: QComboBox, time_config: list):
        self.p_window: "MainWindow" = p_window
        self.day: int = datetime.now().isoweekday()
        self.day_widget: QComboBox = day_widget
        self.day_widget.setCurrentIndex(self.day - 1)
        self.time_config: list = time_config
