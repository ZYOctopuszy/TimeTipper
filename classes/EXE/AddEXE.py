if __name__ == "__main__":
    from main_class import MainWindow
from pathlib import Path

from PySide6.QtWidgets import QApplication, QFileDialog
from loguru import logger

from classes.basic_classes.AddItem import AddItem
from public_functions import kill_exes


class AddEXE(AddItem):
    """
    自定义添加待杀程序窗口类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow") -> None:
        super().__init__(p_window=p_window, list_widget=p_window.ui.for_kill_list)
        self.p_window.ui.remove_exe.clicked.connect(self.remove_item)
        self.p_window.ui.add_exe.clicked.connect(self.add_item_function)
        self.p_window.ui.choose_exe.clicked.connect(self.add_exe_by_choose_file)
        self.ui.get_exe_name.returnPressed.connect(self.add_item_func)
        self.p_window.ui.for_kill_list.itemDoubleClicked.connect(
            self.item_double_clicked_action
        )
        self.ui.label.setText("添加待杀程序")

    @logger.catch
    def add_exe_by_choose_file(self) -> None:
        """
        通过选择文件添加待杀程序
        :return: 无
        """
        file_name = Path(
            QFileDialog.getOpenFileName(parent=self.p_window, caption="选择待杀程序", dir="", filter="*.exe")[0]
        ).name
        if file_name.strip() != "":
            self.p_window.ui.for_kill_list.addItem(file_name)
            logger.debug(f"已添加待杀程序: {file_name}")
        self.p_window.flash_state_changed()

    @logger.catch
    def item_double_clicked_action(self) -> None:
        """
        双击待杀程序列表项时执行
        :return:
        """
        QApplication.processEvents()
        kill_exes(processes=(self.p_window.ui.for_kill_list.currentItem().text()))
