if __name__ == "__main__":
    from MainWindow import MainWindow

from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QAction, QIcon
import keyboard
from loguru import logger


class Tray(QSystemTrayIcon):
    """
    系统托盘图标类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow"):
        super().__init__()
        self.p_window = p_window

        self.setToolTip("那刻夏")

        self.menu = QMenu()

        # 显示与隐藏设置窗口
        self.show_or_hide_action = QAction("呼叫")
        self.show_or_hide_action.setToolTip("与那刻夏交谈")
        self.show_or_hide_action.triggered.connect(self.show_or_hide_func)

        # 启用与禁用提醒
        self.enable_or_disable_action = QAction("催眠")
        self.enable_or_disable_action.setToolTip("催眠那刻夏")
        self.enable_or_disable_action.triggered.connect(
            self.p_window.status_changed_signal.emit
        )

        # 退出应用
        self.exit_action = QAction("道别")
        self.exit_action.setToolTip("离开那刻夏")
        self.exit_action.triggered.connect(self.p_window.exit_app)

        # 将菜单项添加到系统托盘菜单
        self.menu.addActions(
            (self.show_or_hide_action, self.enable_or_disable_action, self.exit_action)
        )

        # 应用系统托盘菜单
        self.activated.connect(self.toggle_tray)
        self.setContextMenu(self.menu)
        self.set_icon()
        self.refresh_tray()

        self.p_window.window_hide_signal.connect(lambda: self.refresh_tray())

    @logger.catch
    def show_or_hide_func(self):
        """
        显示或隐藏设置窗口
        :return:
        """
        if self.p_window.isVisible():
            self.p_window.hide()
        else:
            self.p_window.show()

    @logger.catch
    def refresh_tray(self):
        """
        刷新系统托盘图标状态
        :return:
        """
        if self.p_window.isVisible():
            self.show_or_hide_action.setText("隐藏")
            self.show_or_hide_action.setToolTip("隐藏那刻夏")
        else:
            self.show_or_hide_action.setText("呼叫")
            self.show_or_hide_action.setToolTip("与那刻夏交谈")
        self.enable_or_disable_action.setText(
            "催眠" if self.p_window.status else "唤醒"
        )
        self.enable_or_disable_action.setToolTip(
            "催眠那刻夏" if self.p_window.status else "唤醒那刻夏"
        )

        self.set_icon()

        match self.p_window.config.tray_hide_mode:
            case 0:
                self.setContextMenu(self.menu)
                self.show()
            case 1:
                self.setContextMenu(QMenu())
                self.show()
            case 2:
                self.hide()

    @logger.catch
    def set_icon(self):
        """
        设置系统托盘图标
        :return:
        """
        if self.p_window.config.tray_hide_mode == 1:
            self.setIcon(QIcon(self.p_window.img_files[3]))
        else:
            self.setIcon(QIcon(self.p_window.img_files[0 if self.p_window.status else 1]))

    @logger.catch
    def toggle_tray(self, reason: QSystemTrayIcon.ActivationReason):
        """
        处理点击事件
        :param reason: 激活原因
        :return: 无
        """
        # 托盘双击操作-打开设置窗口
        match reason:
            case QSystemTrayIcon.ActivationReason.Trigger:
                self.p_window.status_changed_signal.emit()
            case QSystemTrayIcon.ActivationReason.DoubleClick:
                self.p_window.status_changed_signal.emit()
                if (
                    not self.p_window.config.tray_hide_mode
                    or keyboard.is_pressed("shift+Esc")
                    and not self.p_window.isVisible()
                ):
                    self.show_or_hide_action.setText("完成")
                    self.show_or_hide_action.setToolTip("结束谈话")
                    self.p_window.show()
                elif self.p_window.isVisible():
                    self.show_or_hide_action.setText("呼叫")
                    self.show_or_hide_action.setToolTip("与那刻夏交谈")
                    self.p_window.hide()

            case QSystemTrayIcon.ActivationReason.MiddleClick:
                self.p_window.exit_app()
