if __name__ == "__main__":
    from MainWindow import MainWindow
from PySide6.QtWidgets import QApplication, QListWidget
from PySide6.QtCore import Qt
from loguru import logger

from classes.basic_classes.GetInput import GetInput


class AddItem(GetInput):
    """
    自定义添加项窗口类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow", list_widget: "QListWidget"):
        super().__init__(p_window, list_widget)

    @logger.catch
    def remove_item(self):
        """
        删除选中项
        :return:
        """
        QApplication.processEvents()
        try:
            self.list_widget.takeItem(self.list_widget.currentRow())
            self.p_window.update_config()
        except Exception as error:
            logger.warning(f"删除项失败{error}")

    @logger.catch
    def add_item_func(self):
        """
        添加项到列表
        :return:
        """
        QApplication.processEvents()
        self.hide()
        new_item = self.ui.get_exe_name.text().strip()
        if new_item  != "" and new_item not in self.list_widget.findItems(new_item, Qt.MatchFlag.MatchExactly):
            self.list_widget.addItem(self.ui.get_exe_name.text())
            self.list_widget.sortItems()
            self.p_window.update_config()

    @logger.catch
    def add_item_function(self):
        """
        处理手动添加项
        :return:
        """
        # 显示程序名称输入框
        self.show()
        self.ui.get_exe_name.clear()
