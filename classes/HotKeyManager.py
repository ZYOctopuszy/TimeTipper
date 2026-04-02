if __name__ == "__main__":
    from MainWindow import MainWindow
import keyboard
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget
from loguru import logger


class HotKeyManager(QWidget):
    """
    热键管理类
    """

    show_window_signal = Signal()

    @logger.catch
    def __init__(self, p_window: "MainWindow"):
        super().__init__()
        self.p_window = p_window

        self.show_window_signal.connect(self.p_window.show_window)

        keyboard.add_hotkey(
            hotkey="ctrl+windows+shift+s", callback=self.show_window
        )
        keyboard.add_hotkey(
            hotkey="ctrl+windows+shift+c", callback=lambda: self.show_status_tip()
        )
        keyboard.add_hotkey(
            "ctrl+windows+shift+q", self.p_window.ensure_quit_signal.emit
        )

    @logger.catch
    def show_window(self):
        """
        显示设置窗口
        :return:
        """
        if self.p_window.config.hide_tray == 2:
            self.show_window_signal.emit()
        
    @logger.catch
    def show_status_tip(self):
        """
        显示状态提示
        :return:
        """
        self.p_window.status_changed_signal.emit()
        self.p_window.status_manager.switch_times += 1

