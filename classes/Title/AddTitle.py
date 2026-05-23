import contextlib

if __name__ == "__main__":
    from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication, QListWidgetItem
from loguru import logger

from ..basic_classes.AddItem import AddItem
from .GetWindowUnderMouse import GetWindowUnderMouse


class AddTitle(AddItem):
    """
    自定义添加待关闭窗口标题窗口类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow"):
        super().__init__(p_window, p_window.ui.for_close_title)
        self.p_window.ui.remove_title.clicked.connect(self.remove_item)
        self.p_window.ui.add_title.clicked.connect(self.add_item_function)
        self.p_window.ui.for_close_title.itemDoubleClicked.connect(
            self.item_double_clicked_action
        )
        self.ui.get_exe_name.returnPressed.connect(self.add_item_func)
        self.ui.label.setText("添加待关闭窗口标题")
        self.ui.get_exe_name.setPlaceholderText("请输入窗口标题")

        self.collecters = []
        self.collecters.extend(
            GetWindowUnderMouse(self.p_window, _) for _ in QApplication.screens()
        )
        self.p_window.ui.choose_on_screen.clicked.connect(self.add_item_easily)
        for collecter in self.collecters:
            collecter.get_window_signal.connect(self.add_item)

    @logger.catch
    def item_double_clicked_action(self, item: QListWidgetItem):
        """
        双击待关闭窗口列表项时执行
        :return:
        """
        QApplication.processEvents()
        self.p_window.kill_windows((item.text(),))

    def add_item_easily(self):
        """
        通过点击屏幕选取窗口
        """
        for collecter in self.collecters:
            collecter.show()

    def add_item(self, item):
        for collecter in self.collecters:
            collecter.setVisible(False)
        if item not in self.p_window.config.for_kill_window_titles:
            self.list_widget.addItem(item)
            self.list_widget.sortItems()
            self.p_window.update_config()
