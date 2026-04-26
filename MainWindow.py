"""
主设置窗口
"""

from typing import Any

from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtGui import QShortcut, QKeySequence
from dataclasses import dataclass
from loguru import logger
from pathlib import Path
from json import load
import keyboard, sys

from classes import *
from classes.basic_classes import *
from UIs import settings
from public_functions import current_path, set_window_size
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

    status_changed_signal = Signal(bool)

    def __init__(self, app: QApplication) -> None:
        super().__init__(auto_hide=False)
        # region 初始化UI
        self.ui = settings.Ui_Form()
        self.ui.setupUi(Form=self)
        # endregion
        # region 设置窗口属性
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_X11BypassTransientForHint)
        set_window_size(window=self, application=app)
        # endregion
        # region 初始化属性
        self.app = app
        self.status: bool = True
        self.exit_asking: bool = False
        self.life: bool = True
        self.test: bool = False
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
                "EXCEL.Title",
                "EasiCamera.exe",
                "POWERPNT.Title",
                "WINWORD.Title",
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
            random_delay=[0, 30],
            duration=0,
        )
        self.config: Config = Config(**self.default_config.__dict__)
        self.config_path: str = current_path(relative_path="config.json", mode="exe")
        # endregion
        # region 初始化时间表配置
        self.time_config_path: str = current_path(
            relative_path="time_config.json", mode="exe"
        )
        self.time_config: list[list[basic_classes.Clock]] = DayManager.get_config(
            config_json=self.time_config_path
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
                r"icons\active.ico",
                r"icons\active.png",
                r"icons\inactive.png",
                r"icons\hide_tray.png",
            ]
        ]
        # endregion
        # region 写入配置文件
        if Path(self.config_path).is_file():
            with open(file=self.config_path, encoding="utf-8") as f:
                self.load_config(configure=Config(**load(fp=f)))
        # endregion
        self.set_widgets()
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
            return config.__dict__.get(key, self.default_config.__dict__[key])

        self.config = Config(
            tray_hide_mode=get_config_value(config=configure, key="tray_hide_mode"),
            for_kill_exes=get_config_value(config=configure, key="for_kill_exes"),
            for_kill_window_titles=get_config_value(
                config=configure, key="for_kill_window_titles"
            ),
            random_delay=get_config_value(config=configure, key="random_delay"),
            duration=get_config_value(config=configure, key="duration"),
        )

        logger.info(f"配置加载完成: {self.config}")

    @logger.catch
    def set_widgets(self):
        """
        设置窗口控件
        :return: 无
        """
        self.ui.if_tray_hide.setChecked(bool(self.config.tray_hide_mode))
        self.ui.if_strong_hide.setChecked(self.config.tray_hide_mode == 2)
        self.ui.if_tray_hide.setDisabled(self.ui.if_strong_hide.isChecked())
        self.ui.a.setValue(self.config.random_delay[0])
        self.ui.b.setValue(self.config.random_delay[1])
        self.ui.hold_seconds.setValue(self.config.duration)

        for widget in [self.ui.if_tray_hide, self.ui.if_strong_hide]:
            widget.stateChanged.connect(self.set_flushable)
        for widget in [
            self.ui.a,
            self.ui.b,
            self.ui.hold_seconds,
        ]:
            widget.valueChanged.connect(self.set_flushable)
        self.ui.apply_button.clicked.connect(self.flash_state_changed)
        self.ui.is_active.clicked.connect(self.status_changed_signal.emit)
        self.ui.test_button.clicked.connect(lambda: setattr(self, "test", True))
        self.ui.exit_button.clicked.connect(self.exit_app)
        self.ui.if_strong_hide.stateChanged.connect(self.strong_hide_action)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.minimize_button.clicked.connect(self.showMinimized)

    @logger.catch
    def son_classes_init(self):
        """
        初始化子类
        :return: 无
        """
        # region 初始化状态管理器
        self.status_manager = StatusManager(self)
        self.status_changed_signal.connect(self.change_state)
        # endregion

        # region 初始化热键管理器
        self.hot_key_manager = HotKeyManager(self)
        QShortcut(QKeySequence("Alt+A"), self).activated.connect(
            lambda: (
                self.flash_state_changed() if self.ui.apply_button.isEnabled() else None
            )
        )
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.exit_app)
        # endregion

        # region 初始化托盘图标
        self.tray_icon = Tray(self)
        self.tray_icon.flash_tray()
        # endregion

        # region 初始化weekday管理类
        self.day_manager = DayManager(self, self.ui.day, self.time_config)
        # endregion

        # region 初始化时间列表管理器
        self.time_manager = TimeManager(self, self.ui.time_list, self.day_manager.day)
        # endregion

        # region 初始化待杀应用窗口类
        self.add_executable = EXE.AddEXE.AddEXE(p_window=self)
        self.edit_executable = EXE.EditEXE.EditEXE(p_window=self)
        # endregion

        # region 初始化待杀窗口标题类
        self.add_title = Title.AddTitle.AddTitle(p_window=self)
        self.edit_title = Title.EditTitle.EditTitle(p_window=self)
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

    @Slot(bool)
    @logger.catch
    def change_state(self, active: bool):
        """
        切换工作状态
        :param active: 是否工作中
        :return: 无
        """
        self.status = active
        self.ui.is_active.setText("工作中" if self.status else "睡觉中")
        self.tray_icon.change_tray_state()
        self.status_manager.ui.status.setText(str(self.status))

    @Slot()
    @logger.catch
    def exit_app(self):
        """
        退出应用
        :return: 无
        """
        self.life = False
        keyboard.unhook_all()
        logger.warning("正在退出应用...")
        self.status_manager.destroy()
        self.app.quit()
        sys.exit()

    # endregion

    @logger.catch
    def confirm_exit(self):
        """
        确认退出应用
        :return: 无
        """
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
