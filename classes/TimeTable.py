if __name__ == "__main__":
    from main_class import MainWindow

from PySide6.QtWidgets import QHeaderView
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtCore import Qt, QEvent


class TimeTable:
    """
    时间表类
    """

    def __init__(self, p_window: "MainWindow"):
        self.p_window = p_window
        self.time_table = self.p_window.ui.time_table
        # self.time_table.clear()
        self.time_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.time_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        for column in range(self.time_table.columnCount()):
            for row in range(self.time_table.rowCount()):
                if item:=self.time_table.item(row, column):
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setIcon(QIcon(self.p_window.files[0]))
