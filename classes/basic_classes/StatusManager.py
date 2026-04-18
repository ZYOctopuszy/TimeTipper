import contextlib
if __name__ == "__main__":
    from MainWindow import MainWindow
from time import sleep

from ctypes import wintypes
import ctypes
from PySide6.QtGui import QMouseEvent, QCursor
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt, Signal, QTimer
from UIs import status_shower
import threading
from loguru import logger

class StatusManager(QWidget):
    """
    状态管理器类
    """
    show_status_signal = Signal()

    def __init__(self, p_window: "MainWindow") -> None:
        super().__init__()
        self.p_window = p_window
        self.mouse_tracking: bool = False
        self.switch_times: int = 0
        self.user32 = ctypes.windll.user32
        self.ui = status_shower.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint
                            | Qt.WindowType.FramelessWindowHint
                            | Qt.WindowType.SplashScreen
                            | Qt.WindowType.X11BypassWindowManagerHint
                            )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        
        self.mouse_move_timer = QTimer(self)
        self.mouse_move_timer.timeout.connect(self.move_to_mouse)
        self.mouse_move_timer.start(10)


    def move_to_mouse(self):
        """
        将窗口移动到鼠标位置
        :return:
        """
        if not self.switch_times:
            self.switch_times -= 1
            self.show_status()
        if self.mouse_tracking:
            with contextlib.suppress(Exception, KeyboardInterrupt):
                self.raise_()
                self.activateWindow()
                self.move(QCursor.pos())

    @logger.catch
    def show(self) -> None:
        """
        显示状态提示
        :return:
        """
        super().show()
        self.mouse_tracking = True

    @logger.catch
    def show_status(self) -> None:
        """
        显示状态提示
        :return:
        """
        self.ui.status.setText(f"TimeTipper - {str(self.p_window.status)}")
        # self.move(QCursor.pos())
        if not self.isVisible():
            self.show_status_signal.emit()
            threading.Thread(target=self.thread_tasks).start()
    
    @logger.catch
    def thread_tasks(self):
        threading.Thread(target=self.hide_after_three_seconds, daemon=True).start()

    @logger.catch
    def hide_after_three_seconds(self):
        sleep(3)
        self.mouse_tracking = False
        self.setVisible(False)

    