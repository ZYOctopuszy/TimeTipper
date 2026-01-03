import sys
from typing import Self
from json import load, dump
from pathlib import Path

import keyboard
from PySide6.QtCore import Signal, Slot, Qt, QEvent, QTimer
from PySide6.QtGui import QShortcut, QKeySequence
from PySide6.QtWidgets import QApplication, QWidget
from loguru import logger

import classes
from UIs import settings
from classes.WindowCloser import WindowCloser
from public_functions import *

__all__ = ["MainWindow"]


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
        super().__init__(auto_hide=False)
        # 初始化ui
        self.ui = settings.Ui_Form()
        self.ui.setupUi(Form=self)
        self.setWindowTitle("那刻夏")
        set_window_size(window=self, application=app)
        self.app = app
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # 实例化关闭窗口类
        self.window_closer = WindowCloser()
        # 初始化日志管理类
        self.logger_manager = classes.LogManager(self)
        # 软件激活状态
        self.state: bool = True
        # 默认配置文件
        self.default_config: dict = {
            "hide_tray": 0,
            "forKillExe": [
                "EXCEL.Title",
                "EasiCamera.exe",
                "POWERPNT.Title",
                "WINWORD.Title",
                "et.exe",
                "wps.exe",
                "wpscloudsvr.exe",
            ],
            "forKillWindowTitle": [
                ".pdf",
                ".ppt",
                ".pptx",
                ".xlsx",
                "192.168.",
                "分享的图片",
                "聊天记录",
                "文档文件",
            ],
            "random_time": [0, 30],
            "hold_time": 0,
        }
        # 持续时间
        self.hold_time: int = 0
        # 下课时间表
        self.time_config: list[classes.basic_classes.Clock.Clock] = []
        # 软件生命状态
        self.life: bool = True
        # 测试模式
        self.test: bool = False
        # 隐藏托盘图标
        self.hide_tray: int = self.default_config["hide_tray"]
        # 待杀程序列表
        self.forKillExe: list[str] = self.default_config["forKillExe"]
        # 待杀应用窗口标题
        self.forKillWindowTitle: list[str] = self.default_config["forKillWindowTitle"]
        # 随机等待时间
        self.random_time: list[int] = self.default_config["random_time"]
        # 配置文件路径
        self.clock_json_path: str = current_path(relative_path="clock.json", mode="exe")
        self.config_json_path: str = current_path(
            relative_path="config.json", mode="exe"
        )
        logger.debug(f"配置文件路径: {self.clock_json_path}")
        logger.debug(f"配置文件路径: {self.config_json_path}")
        self.files: list[str] = [
            r"icons\active.png",
            r"icons\inactive.png",
            r"icons\hide_tray.png",
            r"icons\active.ico",
        ]
        # 设置图片文件路径
        self.files: list[str] = [
            str(object=Path(i).resolve()) for i in map(current_path, self.files)
        ]
        QShortcut(QKeySequence("Alt+A"), self).activated.connect(
            lambda: (
                self.flash_state_changed() if self.ui.apply_button.isEnabled() else None
            )
        )
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.quit_app)
        # region 处理配置文件
        what_is_the_error: str = "t-error"
        try:
            with open(file=self.clock_json_path, encoding="utf-8") as f:
                d = load(f)
                self.time_config = [
                    classes.basic_classes.Clock.Clock(
                        time=time, description=d[time][0], state=d[time][1]
                    )
                    for time in d.keys()
                ]
                logger.debug(f"下课时间配置: {self.time_config}")
            what_is_the_error = "f-error"
            with open(file=self.config_json_path, encoding="utf-8") as f:
                self.load_config(configure=load(fp=f))
                logger.debug("导入成功")
        except Exception as e:
            match what_is_the_error:
                case "t-error":
                    logger.error(
                        f"时间表配置文件不存在或损坏, 创建默认时间表配置文件{e}"
                    )
                    with open(
                        file=self.clock_json_path, mode="w", encoding="utf-8"
                    ) as f:
                        dump(
                            obj={"00:00": ["Default Description", True]}, fp=f, indent=4
                        )
                    logger.critical(f"严重未知错误, 错误代码: {e}")
                case "f-error":
                    logger.error(f"功能配置文件不存在或损坏, 创建默认配置文件{e}")
                    with open(
                        file=self.config_json_path, mode="w", encoding="utf-8"
                    ) as f:
                        dump(obj=self.default_config, fp=f, indent=4)
                case _:
                    logger.critical(f"严重未知错误, 错误代码: {e}")
                    sys.exit(status=1)
        self.show_config()
        # endregion

        # region 刷新控件状态
        self.ui.if_tray_hide.setChecked(bool(self.hide_tray))
        self.ui.if_strong_hide.setChecked(self.hide_tray == 2)
        self.ui.if_tray_hide.setDisabled(self.ui.if_strong_hide.isChecked())
        self.ui.a.setValue(self.random_time[0])
        self.ui.b.setValue(self.random_time[1])
        self.ui.hold_seconds.setValue(self.hold_time)
        # endregion

        # region 初始化热键管理器
        self.hot_key_manager = classes.HotKeyManager(self)
        # endregion

        # region 初始化时间列表管理器
        self.time_manager = classes.TimeManager(self)
        # endregion

        # region 关联控件函数
        normal_widgets: list[QWidget] = [
            self.ui.if_tray_hide,
            self.ui.if_strong_hide,
            self.ui.a,
            self.ui.b,
            self.ui.hold_seconds,
        ]
        connect_signals(widgets=normal_widgets, func=self.set_flushable)
        self.ui.apply_button.clicked.connect(self.flash_state_changed)
        self.ui.is_active.clicked.connect(self.state_changed_signal.emit)
        self.ui.test_button.clicked.connect(self.testing)
        self.ui.exit_button.clicked.connect(self.quit_app)
        self.ui.if_strong_hide.stateChanged.connect(self.strong_hide_action)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.minimize_button.clicked.connect(self.showMinimized)
        # endregion

        # region 初始化托盘图标
        self.tray_icon = classes.Tray(self)
        self.tray_icon.flash_tray()
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
        self.ui.for_kill_list.addItems(self.forKillExe)
        self.ui.for_close_title.addItems(self.forKillWindowTitle)
        logger.debug("已加载待杀程序列表")
        # endregion

    # region 主窗口类方法s
    # region 重写的方法s
    @logger.catch
    def changeEvent(self, event: QEvent):
        """
        处理窗口最小化行为
        :param event: 事件对象
        :return: 无
        """
        if (
            self.windowState() == Qt.WindowState.WindowMinimized
            and event.type() == QEvent.Type.WindowStateChange
        ):
            logger.debug("设置窗口最小化, 执行隐藏窗口")
            QTimer.singleShot(0, self.hide)
        super().changeEvent(event)

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
    @logger.catch
    @Slot()
    def strong_hide_action(self, state: bool):
        """
        关联强隐藏托盘图标状态
        :param state: 强隐藏状态
        :return:
        """
        self.ui.if_tray_hide.setDisabled(state)
        self.ui.if_tray_hide.setChecked(True)

    @logger.catch
    @Slot()
    def testing(self):
        self.test = True

    @logger.catch
    @Slot()
    def set_flushable(self, *args):
        """
        设置应用按钮为可点击状态
        :return:
        """
        self.ui.apply_button.setEnabled(True)

    @logger.catch
    @Slot()
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
    def load_config(self, configure: dict):
        """
        加载配置
        :param configure: 配置字典
        :return: 无
        """
        QApplication.processEvents()
        self.hide_tray = configure["hide_tray"] or self.default_config["hide_tray"]
        self.forKillExe = configure["forKillExe"] or self.default_config["forKillExe"]
        self.random_time = (
            configure["random_time"] or self.default_config["random_time"]
        )
        self.hold_time = configure["hold_time"] or self.default_config["hold_time"]
        self.forKillWindowTitle = (
            configure["forKillWindowTitle"] or self.default_config["forKillWindowTitle"]
        )

    @logger.catch
    def show_config(self):
        """
        显示配置
        :return: 无
        """
        QApplication.processEvents()
        logger.debug(
            "当前托盘图标透明(0显1透2隐): {}", self.hide_tray, feature="f-strings"
        )
        logger.debug("当前待杀程序: {}", self.forKillExe, feature="f-strings")
        logger.debug("当前随机时间: {}", self.random_time, feature="f-strings")
        logger.debug("当前持续时间: {}", self.hold_time, feature="f-strings")
        logger.debug(
            "当前待杀应用窗口标题: {}", self.forKillWindowTitle, feature="f-strings"
        )

    @logger.catch
    def flash_config(self: Self, configure: dict) -> dict:
        """
        更新配置文件
        :param configure: 配置字典
        :return: 无
        """
        QApplication.processEvents()
        # 将提供的字典对应值设置为当前值
        configure["hide_tray"] = self.hide_tray
        configure["forKillExe"] = self.forKillExe
        configure["random_time"] = self.random_time
        configure["hold_time"] = self.hold_time
        configure["forKillWindowTitle"] = self.forKillWindowTitle
        return configure

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
        self.forKillExe = flash_list_widget(list_widget=self.ui.for_kill_list)
        self.forKillWindowTitle = flash_list_widget(list_widget=self.ui.for_close_title)
        # endregion
        self.hide_tray = (
            2
            if self.ui.if_strong_hide.isChecked()
            else 1 if self.ui.if_tray_hide.isChecked() else 0
        )
        self.hold_time = self.ui.hold_seconds.value()
        # 判断随机时间范围是否正确(whether a<=b or not)
        if self.ui.a.value() > self.ui.b.value():
            # 不正确,则将两个输入框的值调转
            self.random_time[0] = self.ui.b.value()
            self.random_time[1] = self.ui.a.value()
            self.ui.a.setValue(self.random_time[0])
            self.ui.b.setValue(self.random_time[1])
        else:
            # 如果正确,则将两个输入框的值设置为新的值
            self.random_time[0] = self.ui.a.value()
            self.random_time[1] = self.ui.b.value()
        with open(file=self.config_json_path, mode="w") as f:
            dump(
                obj={
                    "hide_tray": self.hide_tray,
                    "forKillExe": self.forKillExe,
                    "random_time": self.random_time,
                    "hold_time": self.hold_time,
                    "forKillWindowTitle": self.forKillWindowTitle,
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
