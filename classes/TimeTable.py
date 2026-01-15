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

    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if item := self.time_table.itemAt(
                self.time_table.viewport().mapFromGlobal(QCursor().pos())
            ):
                if event.button() == Qt.MouseButton.RightButton:
                    row = item.row()
                    column = item.column()
                    # 在这里处理右键点击事件
                    print(f"切换了课程启用状态: {self.time_table.horizontalHeaderItem(column).text()} - {self.time_table.verticalHeaderItem(row).text()} - {item.text()}")