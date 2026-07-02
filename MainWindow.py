"""
主设置窗口
"""

from typing import Any
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QPixmap, QShortcut, QKeySequence
from dataclasses import dataclass
from loguru import logger
from pathlib import Path
from json import load
import keyboard, sys
import webbrowser, signal

from classes import *
from classes.basic_classes import *
from UIs import settings
from public_functions import current_path, set_window_size, save_config, set_window_recordable
from classes.WindowCloser import kill_windows
from classes.LogManager import LogManager

__all__ = ["MainWindow"]


@dataclass
class Config:
    """
    配置类
    """

    tray_hide_mode: int
    for_kill_exes: list[str]
    for_kill_window_titles: list[str]
    random_delay: list[int]
    duration: int


class MainWindow(MyQWidget):
    """
    主设置窗口类
    """

    status_changed_signal = Signal()
    confirm_exit_signal = Signal()
    window_hide_signal = Signal()
    window_show_signal = Signal()

    def __init__(self, app: QApplication) -> None:
        signal.signal(signal.SIGINT, lambda *args: self.exit_app())
        super().__init__(auto_hide=False)
        # region 初始化UI
        self.ui = settings.Ui_Form()
        self.ui.setupUi(Form=self)
        # endregion
        # region 设置窗口属性
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowType_Mask)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.show()
        # QApplication.processEvents()
        set_window_size(window=self, application=app)
        set_window_recordable(window=self, recordable=False)
        # endregion
        # region 初始化属性
        self.app = app
        self.status: bool = True
        self.exit_asking: bool = False
        self.life: bool = True
        self.testing: bool = False
        # endregion
        # region 实例化关闭窗口方法
        self.kill_windows = kill_windows
        # endregion
        # region 实例化日志管理类
        self.log_manager = LogManager(self)
        # endregion
        # region 初始化配置
        self.default_config = Config(
            tray_hide_mode=0,
            for_kill_exes=[
                "excel.exe",
                "easicamera.exe",
                "powerpnt.exe",
                "winword.exe",
                "et.exe",
                "wps.exe",
                "wpscloudsvr.exe",
            ],
            for_kill_window_titles=[
                ".pdf",
                ".ppt",
                ".pptx",
                ".xlsx",
                "192.168.",
                "分享的图片",
                "聊天记录",
                "文档文件",
            ],
            random_delay=[0, 0],
            duration=1,
        )
        self.config: Config = Config(**self.default_config.__dict__)
        self.config_path: str = current_path(relative_path="config.json", mode="exe")
        # endregion
        # region 初始化时间表配置
        self.time_config_path: str = current_path(
            relative_path="time_config.json", mode="exe"
        )
        self.time_config: list[list[basic_classes.Clock]] = DayManager.get_time_config(
            config_json_path=self.time_config_path
        )
        # endregion
        # region 输出配置文件路径
        logger.info(f"时间表配置文件路径: {self.time_config_path}")
        logger.info(f"软件设置配置文件路径: {self.config_path}")
        # endregion
        # region 设置图片路径
        self.img_files: list[str] = [
            str(object=Path(current_path(relative_path=i)).resolve())
            for i in [
                r"icons\active.png",
                r"icons\inactive.png",
                r"icons\hide_tray.png",
            ]
        ]
        # 设置软件设置窗口的图标
        icon = QPixmap(self.img_files[0]).scaled(
            64,
            64,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.setWindowIcon(icon)
        self.ui.show_icon.setPixmap(icon)
        # endregion
        # region 写入配置文件
        if Path(self.config_path).is_file():
            with open(file=self.config_path, encoding="utf-8") as f:
                try:
                    self.load_config(configure=Config(**load(fp=f)))
                except Exception:
                    self.load_config(configure=self.default_config)
        # endregion
        self.widgets_init()
        self.son_classes_init()

    @logger.catch
    def load_config(self, configure: Config):
        """
        从配置类导入配置
        :param configure: 配置类
        :return: 无
        """

        def get_config_value(config: Config, key: str) -> Any:
            """
            从配置字典中获取值
            :param config: 配置字典
            :param key: 键名
            :return: 键对应的值
            """
            result = config.__dict__.get(key, self.default_config.__dict__[key])
            match key:
                case "tray_hide_mode":
                    if (type(result) is not int) or (result not in [0, 1, 2]):
                        result = self.default_config.tray_hide_mode
                case "random_delay":
                    if type(result) is list and len(result) == 2:
                        for i in range(2):
                            if type(result[i]) is int and result[i] < 0:
                                result[i] = 0
                        if result[0] > result[1]:
                            result[0], result[1] = result[1], result[0]
                case "duration":
                    if type(result) is not int or result < 1:
                        result = self.default_config.duration
            return result

        self.config = Config(
            tray_hide_mode=get_config_value(config=configure, key="tray_hide_mode"),
            for_kill_exes=get_config_value(config=configure, key="for_kill_exes"),
            for_kill_window_titles=get_config_value(
                config=configure, key="for_kill_window_titles"
            ),
            random_delay=get_config_value(config=configure, key="random_delay"),
            duration=get_config_value(config=configure, key="duration"),
        )

    @logger.catch
    def set_widgets_value(self):
        """
        将控件的值设置为存储的值
        """
        self.ui.if_tray_hide.setChecked(bool(self.config.tray_hide_mode))
        self.ui.if_strong_hide.setChecked(self.config.tray_hide_mode == 2)
        self.ui.if_tray_hide.setDisabled(self.ui.if_strong_hide.isChecked())
        self.ui.a.setValue(self.config.random_delay[0])
        self.ui.b.setValue(self.config.random_delay[1])
        self.ui.hold_seconds.setValue(self.config.duration)

    @logger.catch
    def widgets_init(self):
        """
        设置窗口控件
        :return: 无
        """
        self.set_widgets_value()
        for widget in [self.ui.if_tray_hide, self.ui.if_strong_hide]:
            widget.stateChanged.connect(self.set_as_applicable)
        for widget in [
            self.ui.a,
            self.ui.b,
            self.ui.hold_seconds,
        ]:
            widget.valueChanged.connect(self.set_as_applicable)
        self.ui.commandLinkButton.clicked.connect(
            lambda: webbrowser.open("https://github.com/ZYOctopuszy/TimeTipper")
        )
        self.ui.apply_button.clicked.connect(lambda: self.update_config())
        self.ui.is_active.clicked.connect(self.status_changed_signal.emit)
        self.ui.test_button.clicked.connect(lambda: setattr(self, "testing", True))
        self.ui.exit_button.clicked.connect(self.exit_app)
        self.ui.if_strong_hide.stateChanged.connect(self.set_as_applicable)
        self.ui.if_strong_hide.checkStateChanged.connect(
            lambda: self.ui.if_tray_hide.setDisabled(self.ui.if_strong_hide.isChecked())
        )
        self.ui.if_strong_hide.checkStateChanged.connect(
            lambda: (
                self.ui.if_tray_hide.setChecked(True)
                if self.ui.if_strong_hide.isChecked()
                else None
            )
        )
        self.ui.close_button.clicked.connect(self.hide)

        self.status_changed_signal.connect(self.change_state)

    @logger.catch
    def son_classes_init(self):
        """
        初始化子类
        :return: 无
        """
        # # region 初始化状态管理器
        self.status_manager = StatusManager(self)
        # # endregion

        # region 初始化热键管理器
        self.hot_key_manager = HotKeyManager(self)
        QShortcut(QKeySequence("Alt+A"), self).activated.connect(
            lambda: (self.update_config() if self.ui.apply_button.isEnabled() else None)
        )
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.exit_app)
        # endregion

        # region 初始化托盘图标
        self.tray_icon = Tray(self)
        # self.tray_icon.refresh_tray()
        # endregion

        # region 初始化weekday管理类
        self.day_manager = DayManager(self, self.ui.day, self.time_config)
        # endregion

        # region 初始化时间列表管理器
        self.time_manager = ClockManager(self, self.ui.time_list, self.day_manager.day)
        # endregion

        # region 初始化待杀应用窗口类
        self.add_executable = EXE.AddEXE(p_window=self)
        self.edit_executable = EXE.EditEXE(p_window=self)
        # endregion

        # region 初始化待杀窗口标题类
        self.add_title = Title.AddTitle(p_window=self)
        self.edit_title = Title.EditTitle(p_window=self)
        # endregion

        # region 初始化消息提示类
        self.warner = MessageShower(p_window=self)
        # endregion

        # region 初始化待杀程序列表
        self.ui.for_kill_list.addItems(self.config.for_kill_exes)
        self.ui.for_close_title.addItems(self.config.for_kill_window_titles)
        logger.info("已加载待杀程序列表")
        # endregion

    # region 槽函数

    @Slot()
    @logger.catch
    def change_state(self, *args):
        """
        切换工作状态
        :return: 无
        """
        self.status ^= True
        self.ui.is_active.setText("工作中" if self.status else "睡觉中")
        self.status_manager.ui.status.setText(
            f"TimeTipper - {'工作中' if self.status else '睡觉中'}"
        )
        self.tray_icon.refresh_tray()

    @Slot()
    @logger.catch
    def exit_app(self, *args):
        """
        退出应用
        :return: 无
        """
        self.life = False
        keyboard.unhook_all()
        logger.warning("正在退出应用...")
        # self.status_manager.destroy()
        self.app.quit()
        sys.exit()

    @Slot()
    @logger.catch
    def confirm_exit(self, *args):
        """
        确认退出应用
        :return: 无
        """
        self.hot_key_manager.try_exit_times += 1
        if self.hot_key_manager.try_exit_times == 3:
            self.exit_app()

        if not self.exit_asking:
            self.exit_asking = True
            if (
                QMessageBox.question(
                    self,
                    "真的要退出吗?",
                    "真的要退出吗?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                )
                == QMessageBox.StandardButton.Yes
            ):
                self.exit_app()
            self.exit_asking = False
            self.hot_key_manager.try_exit_times = 0

    @Slot()
    @logger.catch
    def update_config(self, *args):
        """
        更新配置
        :return: 无
        """
        self.config.tray_hide_mode = (
            2
            if self.ui.if_strong_hide.isChecked()
            else 1 if self.ui.if_tray_hide.isChecked() else 0
        )
        self.tray_icon.refresh_tray()
        self.config.duration = self.ui.hold_seconds.value()
        if self.ui.a.value() < self.ui.b.value():
            self.config.random_delay[0] = self.ui.a.value()
            self.config.random_delay[1] = self.ui.b.value()
        else:
            self.config.random_delay[0] = self.ui.b.value()
            self.config.random_delay[1] = self.ui.a.value()
        self.config.for_kill_exes = [
            self.ui.for_kill_list.item(row).text()
            for row in range(self.ui.for_kill_list.count())
        ]
        self.config.for_kill_window_titles = [
            self.ui.for_close_title.item(row).text()
            for row in range(self.ui.for_close_title.count())
        ]
        self.set_widgets_value()
        save_config(self.config_path, self.config.__dict__)
        self.ui.apply_button.setDisabled(True)

    @Slot()
    @logger.catch
    def set_as_applicable(self, *args):
        """
        设置为可应用状态
        :return: 无
        """
        self.ui.apply_button.setEnabled(True)

    # endregion

    # region 重写的函数
    def hideEvent(self, event, /):
        self.window_hide_signal.emit()
        event.accept()

    def minimizeEvent(self, event, /):
        event.ignore()

    def closeEvent(self, event, /):
        self.hide()
        event.ignore()

    # endregion
