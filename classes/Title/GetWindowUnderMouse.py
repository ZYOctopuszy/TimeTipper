if __name__ == "__main__":
    from MainWindow import MainWindow
from typing import Any

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QScreen
import win32gui
from loguru import logger


class WindowGetter(QWidget):

    get_window_signal = Signal(str)

    def __init__(self, p_window: "MainWindow", screen: QScreen):
        super().__init__()
        self.p_window = p_window
        self.should_show_screen = screen
        self.setWindowTitle("")
        self.setWindowFlags(
            Qt.WindowType.Window
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.BypassWindowManagerHint
            | Qt.WindowType.WindowDoesNotAcceptFocus
        )
        self.setWindowOpacity(0.01)
        self.setCursor(Qt.CursorShape.CrossCursor)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating, True)

    def show(self):
        super().show()
        self.setWindowState(Qt.WindowState.WindowFullScreen)
        self.move(self.should_show_screen.geometry().topLeft())

    def mousePressEvent(self, *args: Any, **kwargs: Any):
        self.setVisible(False)
        self.get_window()

    def get_window(self):
        hwnd = win32gui.WindowFromPoint(win32gui.GetCursorPos())
        while p_hwnd := win32gui.GetParent(hwnd):
            hwnd = p_hwnd
        self.get_window_signal.emit(win32gui.GetWindowText(hwnd))
        logger.debug(f"已获取当前窗口标题: {win32gui.GetWindowText(hwnd)}")
