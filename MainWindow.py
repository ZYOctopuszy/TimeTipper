"""
主窗口类
"""

from dataclasses import dataclass
import sys
from typing import Self
from json import load, dump
from pathlib import Path

import keyboard
from PySide6.QtCore import Signal, Slot, Qt, QEvent
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QShortcut, QKeySequence
from loguru import logger

import classes
from UIs import settings
from classes.WindowCloser import kill_windows
from public_functions import *

__all__ = ["MainWindow"]


@dataclass
class Config:
    hide_tray: int
    forKillExe: list[str]
    forKillWindowTitle: list[str]
    random_time: list[int]
    hold_time: int


# noinspection PyAttributeOutsideInit
class MainWindow(classes.basic_classes.MyQWidget.MyQWidget):
    """
    自定义主窗口类
    """

    # 定义应用信号
    apply_signal = Signal()
    state_changed_signal = Signal()
    hide_window_signal = Signal()

    @logger.catch
    def __init__(self, app: QApplication):
        super().__init__(False)
        # 初始化ui
        self.ui = settings.Ui_Form()
        self.ui.setupUi(self)  # type: ignore
        self.app = app
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        set_window_size(window=self, application=app)
        # 实例化关闭窗口方法
        self.kill_windows = kill_windows
        # 初始化日志管理类
        self.logger_manager = classes.LogManager(self)
        # 软件激活状态
        self.state: bool = True
        # 默认配置文件
        self.default_config = Config(
            hide_tray=0,
            forKillExe=[
                "EXCEL.Title",
                "EasiCamera.exe",
                "POWERPNT.Title",
                "WINWORD.Title",
                "et.exe",
                "wps.exe",
                "wpscloudsvr.exe",
            ],
            forKillWindowTitle=[
                ".pdf",
                ".ppt",
                ".pptx",
                ".xlsx",
                "192.168.",
                "分享的图片",
                "聊天记录",
                "文档文件",
            ],
            random_time=[0, 30],
            hold_time=0,
        )
        self.config: Config = Config(**self.default_config.__dict__)
        # 下课时间表
        self.clock_json_path: str = current_path(relative_path="clock.json", mode="exe")
        self.time_config: list[list[classes.basic_classes.Clock.Clock]] = (
            classes.DayManager.get_config(config_json=self.clock_json_path)
        )
        # 软件生命状态
        self.life: bool = True
        # 测试模式
        self.test: bool = False
        # 配置文件路径
        self.config_json_path: str = current_path(
            relative_path="config.json", mode="exe"
        )
        logger.debug(f"配置文件路径: {self.clock_json_path}")
        logger.debug(f"配置文件路径: {self.config_json_path}")
        # 设置图片文件路径
        self.files: list[str] = [
            str(object=Path(current_path(relative_path=i)).resolve())
            for i in [
                r"icons\active.png",
                r"icons\inactive.png",
                r"icons\hide_tray.png",
                r"icons\active.ico",
            ]
        ]
        # region 处理配置文件
        if Path(self.config_json_path).exists():
            with open(file=self.config_json_path, encoding="utf-8") as f:
                self.load_config(configure=load(fp=f))  # type: ignore
        self.show_config()
        # endregion

        self.set_widgets()

        self.son_classes_init()

    # region 主窗口类方法s
    # region 重写的方法s
    @logger.catch
    def hideEvent(self, event: QEvent, /):
        self.hide_window_signal.emit()
        event.accept()

    @logger.catch
    def closeEvent(self, event: QEvent, /):
        """
        窗口收到关闭事件时隐藏设置窗口
        :param event: 事件对象
        :return: 无
        """
        self.showMinimized()
        event.ignore()

    # endregion
    # region 槽函数s
    @Slot()
    @logger.catch
    def strong_hide_action(self, state: bool):
        """
        关联强隐藏托盘图标状态
        :param state: 强隐藏状态
        :return:
        """
        self.ui.if_tray_hide.setDisabled(state)
        self.ui.if_tray_hide.setChecked(True)

    @Slot()
    @logger.catch
    def set_flushable(self, *args, **kwargs):  # type: ignore
        """
        设置应用按钮为可点击状态
        :return:
        """
        self.ui.apply_button.setEnabled(True)

    @Slot()
    @logger.catch
    def quit_app(self):
        """
        退出软件
        :return: 无
        """
        self.life = False
        keyboard.unhook_all()
        logger.debug(f"当前软件生命状态: {self.life}")
        self.app.quit()
        sys.exit()

    # endregion

    @logger.catch
    def son_classes_init(self):
        """
        初始化子类
        :return: 无
        """
        # region 初始化热键管理器
        self.hot_key_manager = classes.HotKeyManager(self)
        QShortcut(QKeySequence("Alt+A"), self).activated.connect(
            lambda: (
                self.flash_state_changed() if self.ui.apply_button.isEnabled() else None
            )
        )
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.quit_app)
        # endregion

        # region 初始化托盘图标
        self.tray_icon = classes.Tray(self)
        self.tray_icon.flash_tray()
        # endregion

        # region 初始化weekday管理类
        self.day_manager = classes.DayManager(self, self.ui.day, self.time_config)
        # endregion

        # region 初始化时间列表管理器
        self.time_manager = classes.TimeManager(
            self, self.ui.time_list, self.day_manager.day
        )
        # endregion

        # region 初始化待杀应用窗口类
        self.add_executable = classes.EXE.AddEXE.AddEXE(p_window=self)
        self.edit_executable = classes.EXE.EditEXE.EditEXE(p_window=self)
        # endregion

        # region 初始化待杀窗口标题类
        self.add_title = classes.Title.AddTitle.AddTitle(p_window=self)
        self.edit_title = classes.Title.EditTitle.EditTitle(p_window=self)
        # endregion

        # region 初始化消息提示类
        self.warner = classes.MessageShower(p_window=self)
        # endregion

        # region 初始化待杀程序列表
        self.ui.for_kill_list.addItems(self.config.forKillExe)
        self.ui.for_close_title.addItems(self.config.forKillWindowTitle)
        logger.debug("已加载待杀程序列表")
        # endregion

    @logger.catch
    def set_widgets(self):
        """
        设置窗口控件
        :return: 无
        """
        self.ui.if_tray_hide.setChecked(bool(self.config.hide_tray))
        self.ui.if_strong_hide.setChecked(self.config.hide_tray == 2)
        self.ui.if_tray_hide.setDisabled(self.ui.if_strong_hide.isChecked())
        self.ui.a.setValue(self.config.random_time[0])
        self.ui.b.setValue(self.config.random_time[1])
        self.ui.hold_seconds.setValue(self.config.hold_time)

        for widget in [self.ui.if_tray_hide, self.ui.if_strong_hide]:
            widget.stateChanged.connect(self.set_flushable)
        for widget in [
            self.ui.a,
            self.ui.b,
            self.ui.hold_seconds,
        ]:
            widget.valueChanged.connect(self.set_flushable)
        self.ui.apply_button.clicked.connect(self.flash_state_changed)
        self.ui.is_active.clicked.connect(self.state_changed_signal.emit)
        self.ui.test_button.clicked.connect(lambda: setattr(self, "test", True))
        self.ui.exit_button.clicked.connect(self.quit_app)
        self.ui.if_strong_hide.stateChanged.connect(self.strong_hide_action)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.minimize_button.clicked.connect(self.showMinimized)

    @logger.catch
    def load_config(self, configure: dict):  # type: ignore
        """
        加载配置
        :param configure: 配置字典
        :return: 无
        """
        self.config.hide_tray = configure.get("hide_tray", self.default_config.hide_tray)  # type: ignore
        self.config.forKillExe = configure.get("forKillExe", self.default_config.forKillExe)  # type: ignore
        self.config.random_time = configure.get(  # type: ignore
            "random_time", self.default_config.random_time  # type: ignore
        )
        self.config.hold_time = configure.get("hold_time", self.default_config.hold_time)  # type: ignore
        self.config.forKillWindowTitle = configure.get(  # type: ignore
            "forKillWindowTitle", self.default_config.forKillWindowTitle  # type: ignore
        )

    @logger.catch
    def show_config(self):
        """
        显示配置
        :return: 无
        """
        QApplication.processEvents()
        logger.debug(f"当前托盘图标透明(0显1透2隐): {self.config.hide_tray}")
        logger.debug(f"当前待杀程序: {self.config.forKillExe}")
        logger.debug(f"当前随机时间: {self.config.random_time}")
        logger.debug(f"当前持续时间: {self.config.hold_time}")
        logger.debug(f"当前待杀应用窗口标题: {self.config.forKillWindowTitle}")

    @logger.catch
    def show_window(self: Self):
        """
        显示窗口(获取焦点+活动+前置)
        :return:
        """
        self.setVisible(True)
        self.showNormal()
        self.raise_()
        self.activateWindow()
        self.setFocus()

    @logger.catch
    def change_window_state(self, hide: bool = False):
        """
        显示或隐藏设置窗口
        :param hide:
        :return:
        """
        if hide:
            self.showMinimized()
        else:
            self.show_window()

    @logger.catch
    def flash_state_changed(self):
        """
        刷新配置
        :return: 无
        """
        QApplication.processEvents()
        # 将当前属性设置为GUI控件的值
        # region 设置待杀程序列表 和 待杀应用程序窗口标题列表
        self.config.forKillExe = flash_list_widget(list_widget=self.ui.for_kill_list)
        self.config.forKillWindowTitle = flash_list_widget(
            list_widget=self.ui.for_close_title
        )
        # endregion
        self.config.hide_tray = (
            2
            if self.ui.if_strong_hide.isChecked()
            else 1 if self.ui.if_tray_hide.isChecked() else 0
        )
        self.hold_time = self.ui.hold_seconds.value()
        # 判断随机时间范围是否正确(whether a<=b or not)
        if self.ui.a.value() > self.ui.b.value():
            # 不正确,则将两个输入框的值调转
            self.config.random_time[0] = self.ui.b.value()
            self.config.random_time[1] = self.ui.a.value()
            self.ui.a.setValue(self.config.random_time[0])
            self.ui.b.setValue(self.config.random_time[1])
        else:
            # 如果正确,则将两个输入框的值设置为新的值
            self.config.random_time[0] = self.ui.a.value()
            self.config.random_time[1] = self.ui.b.value()
        with open(file=self.config_json_path, mode="w") as f:
            dump(
                obj={
                    "hide_tray": self.config.hide_tray,
                    "forKillExe": self.config.forKillExe,
                    "random_time": self.config.random_time,
                    "hold_time": self.config.hold_time,
                    "forKillWindowTitle": self.config.forKillWindowTitle,
                },
                fp=f,
                indent=4,
            )
        self.show_config()
        # 将应用按钮设置为禁用状态
        self.ui.apply_button.setDisabled(True)
        # 发送应用信号
        self.apply_signal.emit()

    # endregion
