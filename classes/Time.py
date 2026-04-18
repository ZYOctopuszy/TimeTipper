from PySide6.QtCore import Qt
from loguru import logger

from UIs import add_time
from classes import basic_classes


class Time(basic_classes.MyQWidget.MyQWidget):
    """
    自定义添加时间点窗口类
    """

    @logger.catch
    def __init__(self, use_to: str):
        """
        初始化添加时间点窗口
        :param use_to: 窗口用途, 用于设置窗口标题, 必须为"add_time"或"edit_time"
        """
        super().__init__()
        self.ui = add_time.Ui_Form()
        self.ui.setupUi(self)
        # 设置窗口标志，确保窗口显示在主窗口之上
        self.setWindowFlags(
            # Qt.WindowType.Dialog  # 使用Dialog标志，使其成为模态对话框
             Qt.WindowType.WindowStaysOnTopHint  # 确保保持在顶层
            | Qt.WindowType.FramelessWindowHint  # 无边框
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        (
            self.setWindowTitle("添加时间点")
            if use_to == "add_time"
            else (
                self.setWindowTitle("编辑时间点")
                if use_to == "edit_time"
                else exec(
                    "raise ValueError('use_to must be 'add_time' or 'edit_time'')"
                )
            )
        )
        self.hide()

    def show(self):
        """
        重写show方法，确保窗口显示在最顶层
        """
        super().show()
        self.raise_()
        self.activateWindow()
