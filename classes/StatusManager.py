if __name__ == "__main__":
    from MainWindow import MainWindow
import time

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, QMetaObject
from UIs import status_shower
import threading
from loguru import logger


class StatusManager(QWidget):
    """
    状态管理器类
    """

    def __init__(self, p_window: "MainWindow") -> None:
        super().__init__()
        self.p_window = p_window

        self.ui = status_shower.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(
            Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.SplashScreen
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)

        # 线程控制标志
        self._time = 0
        self._update_position()

        # 默认隐藏
        self.hide()

    @logger.catch
    def show_status(self) -> None:
        """
        显示状态提示（固定在屏幕顶部）
        """

        # 3秒后自动隐藏
        self._time = 3
        if not self.isVisible():
            # 立即显示窗口（固定在屏幕顶部居中）
            QMetaObject.invokeMethod(self, "show", Qt.ConnectionType.QueuedConnection)
            # 自动隐藏
            target=threading.Thread(
                target=self._auto_hide_task, daemon=True
            ).start()

    def _update_position(self) -> None:
        """
        更新窗口位置到屏幕顶部居中
        """
        # 获取屏幕几何信息
        screen_geometry = self.screen().geometry()
        screen_width = screen_geometry.width()
        screen_top = screen_geometry.top()

        # 计算窗口位置（屏幕顶部居中）
        window_width = self.width()
        offset_y = 20  # 距离顶部的偏移
        new_x = (screen_width - window_width) // 2  # 水平居中
        new_y = screen_top + offset_y  # 顶部偏移

        # 移动窗口
        self.move(new_x, new_y)

    def _auto_hide_task(self) -> None:
        """
        3秒后自动隐藏窗口
        """
        while self._time > 0:
            time.sleep(1)
            self._time -= 1
        if self.isVisible():
            QMetaObject.invokeMethod(self, "hide", Qt.ConnectionType.QueuedConnection)
