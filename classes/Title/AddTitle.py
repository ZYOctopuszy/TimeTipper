if __name__ == "__main__":
    from main_classes import MainWindow
from PySide6.QtWidgets import QApplication
from loguru import logger

from classes.basic_classes.AddItem import AddItem


class AddTitle(AddItem):
    """
    自定义添加待关闭窗口标题窗口类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow"):
        super().__init__(p_window, p_window.ui.for_close_title)
        self.p_window.ui.remove_title.clicked.connect(self.remove_item)
        self.p_window.ui.add_title.clicked.connect(self.add_item_function)
        self.ui.get_exe_name.returnPressed.connect(self.add_item_func)
        self.ui.label.setText("添加待关闭窗口标题")
        self.ui.get_exe_name.setPlaceholderText("请输入窗口标题")

    @logger.catch
    def item_double_clicked_action(self):
        """
        双击待关闭窗口列表项时执行
        :return:
        """
        QApplication.processEvents()
        self.p_window.window_closer.kill_windows(
            self.p_window.ui.for_close_title.currentItem().text()
        )
