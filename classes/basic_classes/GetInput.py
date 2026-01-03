if __name__ == "__main__":
    from main_class import MainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from loguru import logger

from classes.basic_classes.MyQWidget import MyQWidget

from UIs import get_input
from PySide6.QtWidgets import QListWidget


class GetInput(MyQWidget):
    """
    自定义获取输入窗口类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow", list_widget: QListWidget):
        super().__init__()
        self.ui = get_input.Ui_get_input()
        self.ui.setupUi(self)
        self.p_window = p_window
        self.list_widget = list_widget
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(self.p_window.files[3]))
        self.hide()
