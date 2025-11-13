import sys
import threading
from datetime import datetime, timedelta
from json import load, dump
from os import path
from os.path import split, basename, abspath
from random import randint
from time import sleep

import keyboard
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal, QTime, QObject
from PySide6.QtGui import QIcon, QMouseEvent
from PySide6.QtGui import QPixmap, QAction, QShortcut, QKeySequence
from PySide6.QtWidgets import (
    QMenu,
    QSystemTrayIcon,
    QFileDialog,
    QListWidgetItem,
)

from UIs import get_input
from UIs import settings, add_time
from WindowCloser import WindowCloser
from public_functions import *


class MainWindow(QWidget):
    """
    自定义主窗口类
    """

    # 定义应用信号
    apply_signal = Signal()
    state_changed_signal = Signal()
    hide_window_signal = Signal()

    @logger.catch
    def __init__(self, app: QApplication):
        QApplication.processEvents()
        super().__init__()
        self.app = app
        # 初始化ui
        self.ui = settings.Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("那刻夏")
        set_window_size(self, app)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_PaintOnScreen)
        # 实例化关闭窗口类
        self.window_closer = WindowCloser()
        # 初始化日志管理类
        self.logger_manager = LogManager(self)
        # 软件激活状态
        self.state: bool = True
        # 默认配置文件
        # noinspection SpellCheckingInspection
        self.default_config: dict = {
            "hide_tray": 0,
            "forKillExe": [
                "EXCEL.EXE",
                "EasiCamera.exe",
                "POWERPNT.EXE",
                "WINWORD.EXE",
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
                "\u5206\u4eab\u7684\u56fe\u7247",
                "\u6587\u6863\u6587\u4ef6",
                "\u804a\u5929\u8bb0\u5f55",
            ],
            "random_time": [0, 30],
            "hold_time": 0,
        }
        # 持续时间
        self.hold_time: int = 0
        # 下课时间表
        self.time_config: dict = {}
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
        self.clock_json_path: str = path.join(
            split(abspath(sys.argv[0]))[0], "clock.json"
        )
        self.config_json_path: str = path.join(
            split(abspath(sys.argv[0]))[0], "config.json"
        )
        logger.debug(f"配置文件路径: {self.clock_json_path}")
        logger.debug(f"配置文件路径: {self.config_json_path}")
        QShortcut(QKeySequence("Alt+A"), self).activated.connect(
            lambda: (
                self.flash_state_changed() if self.ui.apply_button.isEnabled() else None
            )
        )
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(self.quit_app)
        # region 初始化时间列表管理器
        self.time_manager = TimeManager(self)
        # endregion
        # region 初始化热键管理器
        self.hot_key_manager = HotKeyManager(self)
        self.hot_key_manager.show_window_signal.connect(self.show_window)
        # endregion
        # region 处理配置文件
        t = 0
        try:
            with open(self.clock_json_path, encoding="utf-8") as f:
                self.time_config = load(f)
                logger.debug(f"下课时间配置: {self.time_config}")
            t = 1
            with open(self.config_json_path, encoding="utf-8") as f:
                self.load_config(load(f))
                logger.debug("导入成功")
        except Exception as e:
            if t == 0:
                logger.error(f"时间表配置文件不存在或损坏, 创建默认时间表配置文件{e}")
                with open(self.clock_json_path, "w") as f:
                    dump({"00:00": "Default Description"}, f, indent=4)
                logger.critical(f"严重未知错误, 错误代码: {e}")
            elif t == 1:
                logger.error(f"功能配置文件不存在或损坏, 创建默认配置文件{e}")
                with open(self.config_json_path, "w") as f:
                    dump(self.default_config, f, indent=4)
            else:
                logger.critical(f"严重未知错误, 错误代码: {e}")
                sys.exit(1)
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
        # region 关联控件函数
        normal_widgets: list = [
            self.ui.if_tray_hide,
            self.ui.if_strong_hide,
            self.ui.a,
            self.ui.b,
            self.ui.hold_seconds,
        ]
        connect_signals(normal_widgets, self.set_flushable)
        self.ui.apply_button.clicked.connect(self.flash_state_changed)
        self.ui.is_active.clicked.connect(self.state_changed_signal.emit)
        self.ui.test_button.clicked.connect(self.testing)
        self.ui.exit_button.clicked.connect(self.quit_app)
        self.ui.if_strong_hide.stateChanged.connect(self.strong_hide_action)
        self.ui.close_button.clicked.connect(self.close)
        self.ui.minimize_button.clicked.connect(self.showMinimized)
        # endregion
        # region 时间点编辑功能实现
        # 检测时间列表选中项改变和描述内容改变
        self.ui.time_list.itemSelectionChanged.connect(
            self.time_manager.flash_description
        )
        self.ui.description.textChanged.connect(self.time_manager.edit_description)
        self.ui.time_list.addItems(list(sorted(self.time_config.keys())))
        # endregion

        # region 初始化托盘图标
        self.tray_icon = MyTray(self)
        self.tray_icon.flash_tray()
        # endregion

        # region 初始化待杀应用窗口类
        self.add_executable = AddEXE(self)
        self.edit_executable = EditEXE(self)
        # endregion

        # region 初始化待杀窗口标题类
        self.add_title = AddTitle(self)
        self.edit_title = EditTitle(self)
        # endregion

        # region 初始化消息提示类
        self.warner = MessageShower(self, self.tray_icon)
        # endregion

        # region 初始化待杀程序列表
        self.ui.for_kill_list.addItems(self.forKillExe)
        self.ui.for_close_title.addItems(self.forKillWindowTitle)
        logger.debug("已加载待杀程序列表")
        # endregion

    # region 主窗口类方法s
    @logger.catch
    def strong_hide_action(self, state):
        """
        关联强隐藏托盘图标
        :return:
        """
        self.ui.if_tray_hide.setDisabled(state)
        self.ui.if_tray_hide.setChecked(True)

    @logger.catch
    def testing(self):
        self.test = True

    @logger.catch
    def set_flushable(self, *args, **kwargs):
        """
        设置应用按钮为可点击状态
        :return:
        """
        self.ui.apply_button.setEnabled(True)

    @logger.catch
    def changeEvent(self, event):
        """
        处理窗口最小化行为
        :param event: 事件对象
        :return: 无
        """
        if self.windowState() == Qt.WindowState.WindowMinimized:
            logger.debug("设置窗口最小化, 执行隐藏窗口")
            self.showNormal()
            self.setVisible(False)
            self.hide_window_signal.emit()
        else:
            super().changeEvent(event)

    @logger.catch
    def closeEvent(self, event):
        """
        窗口收到关闭事件时隐藏设置窗口
        :param event: 事件对象
        :return: 无
        """
        self.setVisible(False)
        event.ignore()

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
    def flash_config(self, configure: dict) -> dict:
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
    def show_window(self):
        """
        显示窗口(获取焦点+活动+前置)
        :return:
        """
        self.setVisible(True)
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
            self.setVisible(False)
        else:
            self.show_window()

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

    @logger.catch
    def flash_state_changed(self):
        """
        刷新配置
        :return: 无
        """
        QApplication.processEvents()
        # 将当前属性设置为GUI控件的值
        # region 设置待杀程序列表 和 待杀应用程序窗口标题列表
        self.forKillExe = flash_list_widget(self.ui.for_kill_list)
        self.forKillWindowTitle = flash_list_widget(self.ui.for_close_title)
        # endregion
        self.hide_tray = (
            2
            if self.ui.if_strong_hide.isChecked()
            else 1 if self.ui.if_tray_hide.isChecked() else 0
        )
        self.hold_time = self.ui.hold_seconds.value()
        # 判断随机时间范围是否正确(whether a<=b or not)
        if self.ui.a.value() > self.ui.b.value():
            # 不正确,则将另一个输入框的值设置为变更的输入框的值
            if self.ui.a.value() != self.random_time[0]:
                self.random_time[0] = self.ui.a.value()
                self.ui.b.setValue(self.random_time[0])
            else:
                self.random_time[1] = self.ui.b.value()
                self.ui.a.setValue(self.random_time[1])
        else:
            # 如果正确,则将两个输入框的值设置为新的值
            self.random_time[0] = self.ui.a.value()
            self.random_time[1] = self.ui.b.value()
        with open("config.json", "w") as f:
            dump(
                {
                    "hide_tray": self.hide_tray,
                    "forKillExe": self.forKillExe,
                    "random_time": self.random_time,
                    "hold_time": self.hold_time,
                    "forKillWindowTitle": self.forKillWindowTitle,
                },
                f,
                indent=4,
            )
        self.show_config()
        # 将应用按钮设置为禁用状态
        self.ui.apply_button.setDisabled(True)
        # 发送应用信号
        self.apply_signal.emit()

    @logger.catch
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            self.drag = True

    @logger.catch
    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    @logger.catch
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag = False

    # endregion


class LogManager(QObject):
    update_log = Signal(str)

    @logger.catch
    def __init__(self, window: MainWindow):
        super().__init__()
        self.window = window
        # self.window.ui.logger.setLineWrapMode(QTextBrowser.LineWrapMode.NoWrap)
        self.update_log.connect(self.window.ui.logger.append)
        logger.add(
            sink=self,
            format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {name} -> {function} -> {line} >>> {message}",
            enqueue=True,
            backtrace=True,
            catch=True,
        )
        self.gun = self.become_colorful(text=" | ")
        self.curser = self.become_colorful(text=" -> ")
        self.three_cursers = self.become_colorful(text=" >>> ")

    @logger.catch
    def write(self, message: str):
        """
        写入日志
        :param message: 日志内容
        :return:
        """
        message = message.splitlines()
        txt_l = message[0].split(" | ")
        txt_l = txt_l[:-1] + txt_l[-1].split(" -> ")
        txt_l = txt_l[:-1] + txt_l[-1].split(" >>> ")

        context = (
                self.become_colorful(text=txt_l[0], color="green") + self.gun  # 时间
                + self.become_colorful(text=txt_l[1], color="blue"
        if txt_l[1] == "DEBUG" else "yellow"
        if txt_l[1] == "WARNING" else "red") + self.gun  # 日志等级
                + self.become_colorful(text=txt_l[2], color="orange") + self.curser  # 文件名
                + self.become_colorful(text=txt_l[3], color="orange") + self.curser  # 函数名
                + self.become_colorful(text=txt_l[4], color="orange") + self.three_cursers  # 行号
                + self.become_colorful(text=txt_l[5], color="cyan")
        )

        if len(message) > 1:
            for line in message[1:]:
                context += "\n<br>" + self.become_colorful(
                    text=line.replace("<", "&lt;").replace(">", "&gt;").replace(" ", "&nbsp;"))

        self.update_log.emit(context)

    @logger.catch
    def become_colorful(self, text: str, color: str = 'red') -> str:
        """
        将文本转换为指定颜色的字体
        :param text: 要转换的文本
        :param color: 字体颜色
        :return: 转换后的文本
        """
        return f"<font color='{color}' face='Cascadia Mono', 'Cascadia Code', 'Microsoft YaHei'>{rf"{text}"}</font>"


class TimeManager:
    """
    管理时间列表
    """

    def __init__(self, window: MainWindow):
        self.window = window
        self.add_time = AddTime('add_time')
        self.edit_time = AddTime('edit_time')

        self.window.ui.add_button.clicked.connect(
            lambda: self.add_time.show() and self.add_time.ui.timeEdit.clear()
        )
        self.window.ui.edit_button.clicked.connect(self.edit_button_action)
        self.window.ui.delete_button.clicked.connect(self.delete_button_action)

        self.add_time.ui.sure.clicked.connect(self.add_button_action)
        self.edit_time.ui.sure.clicked.connect(self.edit_time_function)

    # region 时间编辑功能函数
    @logger.catch
    def add_button_action(self):
        """
        添加提醒时间
        :return: 无
        """
        QApplication.processEvents()
        self.add_time.hide()
        # 格式化时间字符串为"小时:分钟"格式
        if (
                added_time := self.add_time.ui.timeEdit.time().toString("HH:mm")
        ) not in self.window.time_config.keys():
            self.window.time_config[added_time] = "Default Description"
            self.window.ui.time_list.clear()
            self.window.ui.time_list.addItems(sorted(self.window.time_config.keys()))
            self.edit_description()

    @logger.catch
    def delete_button_action(self):
        """
        删除当前选中项
        :return: 无
        """
        QApplication.processEvents()
        if current_item := self.window.ui.time_list.currentItem():
            self.window.ui.time_list.takeItem(
                self.window.ui.time_list.currentRow())
            del self.window.time_config[current_item.text()]
            self.flash_time_config()

    @logger.catch
    def edit_button_action(self):
        """
        显示时间编辑框
        :return:
        """
        QApplication.processEvents()
        if (
                type(current_item := self.window.ui.time_list.currentItem())
                is QListWidgetItem
        ):
            self.edit_time.ui.timeEdit.setTime(
                QTime.fromString(current_item.text(), "HH:mm")
            )
            self.edit_time.show()

    @logger.catch
    def edit_time_function(self):
        """
        编辑选中时间项
        :return:
        """
        self.edit_time.hide()
        before_time: str = self.window.ui.time_list.currentItem().text()
        if (
                new_time := self.edit_time.ui.timeEdit.time().toString("HH:mm")
        ) not in self.window.time_config.keys():
            self.window.ui.time_list.currentItem().setText(new_time)
            self.window.time_config[new_time] = self.window.time_config.pop(
                before_time, None
            )
            self.window.ui.time_list.sortItems()
            self.flash_time_config()

    # endregion

    # region 时间描述操作相关
    @logger.catch
    def flash_description(self):
        """
        展示当前选中项的描述
        :return: 无
        """
        QApplication.processEvents()
        if current_item := self.window.ui.time_list.currentItem():
            logger.debug(f"当前选中: {current_item.text()}")
            self.window.ui.description.setText(
                self.window.time_config[current_item.text()]
            )

    @logger.catch
    def edit_description(self):
        """
        刷新当前选中项的描述
        :return: 无
        """
        QApplication.processEvents()

        if current_item := self.window.ui.time_list.currentItem():
            self.window.time_config[current_item.text()] = (
                self.window.ui.description.toPlainText()
            )
            self.flash_time_config()

    @logger.catch
    def flash_time_config(self):
        """
        刷新时间表配置
        :return:
        """
        self.window.time_config = {k: self.window.time_config[k] for k in sorted(self.window.time_config.keys())}
        logger.debug(f"已刷新时间表配置, 当前配置:{self.window.time_config}")
        with open("clock.json", "w", encoding="utf-8") as f:
            dump(self.window.time_config, f, ensure_ascii=False, indent=4)

    # endregion


class HotKeyManager(QObject):
    """
    热键管理类
    """
    show_window_signal = Signal()

    @logger.catch
    def __init__(self, parent: MainWindow):
        super().__init__()
        self.window = parent
        keyboard.add_hotkey("ctrl+windows+alt+shift+f6", self.show_window)

    @logger.catch
    def show_window(self):
        """
        显示设置窗口
        :return:
        """
        if self.window.hide_tray == 2:
            self.show_window_signal.emit()


class MyTray(QSystemTrayIcon):
    """
    自定义系统托盘图标类
    """

    @logger.catch
    def __init__(self, connect_window: MainWindow):
        QApplication.processEvents()
        super().__init__()
        self.files = [
            r"icons\active.png",
            r"icons\inactive.png",
            r"icons\hide_tray.png",
            r"icons\active.ico",
        ]
        self.connect_window: MainWindow = connect_window

        self.setToolTip("那刻夏")

        self.connect_window.apply_signal.connect(self.flash_tray)
        self.connect_window.state_changed_signal.connect(
            lambda: self.change_tray_state(False)
        )
        self.connect_window.hide_window_signal.connect(self.show_hide_window)

        # 创建系统托盘菜单
        self.menu: QMenu = QMenu()

        # "显示"和"隐藏"菜单项
        self.show_hide_action: QAction = QAction("呼叫")
        self.show_hide_action.setToolTip("与那刻夏交谈")
        self.show_hide_action.triggered.connect(lambda: self.show_hide_window(True))
        self.menu.addAction(self.show_hide_action)

        # "启用与禁用"菜单项
        self.enable_disable_action: QAction = QAction("催眠")
        self.enable_disable_action.setToolTip("催眠那刻夏")
        self.enable_disable_action.triggered.connect(self.change_tray_state)
        self.menu.addAction(self.enable_disable_action)

        # "退出"菜单项
        self.exit_action: QAction = QAction("送别")
        self.exit_action.setToolTip("送别那刻夏")
        self.exit_action.triggered.connect(connect_window.quit_app)
        self.menu.addAction(self.exit_action)

        # 应用系统托盘菜单
        self.setContextMenu(self.menu)
        self.set_picture_path()
        self.show()

        # 连接系统托盘图标点击信号与槽函数
        self.activated.connect(self.toggle_window)

    @logger.catch
    def set_picture_path(self):
        """
        设置系统托盘图标图片路径
        :return:
        """
        QApplication.processEvents()
        # 设置图片文件路径
        file_paths = map(resource_path, self.files)

        self.files = [abspath(i) for i in file_paths]
        self.setIcon(QIcon(self.files[0]))
        self.connect_window.setWindowIcon(QIcon(self.files[0]))
        self.connect_window.ui.show_icon.setPixmap(
            QPixmap(self.files[0]).scaled(
                30,
                30,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

    @logger.catch
    def toggle_window(self, reason):
        """
        实现托盘各种点击操作
        :param reason: 点击类型
        :return: 无
        """
        # 托盘双击操作-打开设置
        QApplication.processEvents()
        if reason == QSystemTrayIcon.ActivationReason.DoubleClick:
            if not self.connect_window.isVisible() and (
                    (not self.connect_window.hide_tray) or keyboard.is_pressed("shift+esc")
            ):
                # 显示设置窗口
                logger.debug("显示设置窗口")
                self.show_hide_action.setText("设完了")
                self.show_hide_action.setToolTip("交流完毕")
                self.connect_window.change_window_state()
            elif self.connect_window.isVisible():
                # 隐藏设置窗口
                self.show_hide_action.setText("呼叫")
                self.show_hide_action.setToolTip("与那刻夏交谈")
                self.connect_window.change_window_state(True)

        # 托盘中建操作-关闭软件
        elif reason == QSystemTrayIcon.ActivationReason.MiddleClick:
            self.connect_window.quit_app()

    @logger.catch
    def change_tray_state(self, change_state: bool = True):
        """
        改变托盘图标状态
        :return:
        """
        if change_state:
            self.connect_window.state ^= True
            self.connect_window.ui.is_active.setText(
                "工作中" if self.connect_window.state else "睡觉中"
            )
            logger.debug(f"当前启用状态: {self.connect_window.state}")
        QApplication.processEvents()
        self.enable_disable_action.setText(
            "催眠" if self.connect_window.state else "唤醒"
        )
        if not self.connect_window.hide_tray:
            logger.debug("托盘图标未设置隐藏, 切换托盘图标图片")
            if self.connect_window.state:
                self.setIcon(QIcon(self.files[0]))
                self.setToolTip("那刻夏")
            else:
                self.setIcon(QIcon(self.files[1]))
                self.setToolTip("那刻夏\n(睡觉中)")

    @logger.catch
    def show_hide_window(self, change_window_state: bool = False):
        """
        改变托盘上下文菜单
        :param change_window_state: 是否改变窗口状态
        :return:
        """
        if change_window_state:
            self.connect_window.change_window_state(self.connect_window.isVisible())
        if self.connect_window.isVisible():
            self.show_hide_action.setToolTip("与那刻夏交谈")
            self.show_hide_action.setText("呼叫")
        else:
            self.show_hide_action.setToolTip("交谈完毕")
            self.show_hide_action.setText("设完了")

    @logger.catch
    def flash_tray(self):
        """
        刷新托盘图标状态
        :return:
        """
        self.setVisible(self.connect_window.hide_tray != 2)
        if self.connect_window.hide_tray == 1:
            self.setToolTip("")
            self.setIcon(QIcon(self.files[2]))
        else:
            self.change_tray_state(False)


class AddTime(QWidget):
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
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
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

    @logger.catch
    def changeEvent(self, event, /):
        if not self.isActiveWindow():
            self.hide()
        super().changeEvent(event)

    @logger.catch
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            self.drag = True

    @logger.catch
    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    @logger.catch
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag = False


class MessageShower:
    """
    自定义消息显示类
    """

    @logger.catch
    def __init__(self, window: MainWindow, tray_icon: QSystemTrayIcon):
        self.window, self.tray_icon = window, tray_icon
        threading.Thread(target=self.warn).start()

    # region 通知提醒功能实现
    @logger.catch
    def warning_action(self):
        """
        当下课时执行的操作(关闭相关软件!)
        :return:
        """
        now = datetime.now()
        wait_second = (
            randint(self.window.random_time[0], self.window.random_time[1])
            if now.strftime("%H:%M") in self.window.time_config.keys()
               or self.window.test
            else 0
        )
        logger.debug(f"将等待时间: {wait_second}秒")
        while self.window.life and self.window.state:
            if datetime.now() - (now + timedelta(seconds=wait_second)) <= timedelta():
                sleep(1)
                continue
            else:
                logger.debug("关闭窗口中")
                mapx(
                    self.window.window_closer.kill_windows,
                    self.window.forKillWindowTitle,
                )
                logger.debug("杀死进程中")
                mapx(kill_exe, self.window.forKillExe)
                break
        self.window.test = False
        self.window.ui.test_button.setEnabled(True)
        self.window.ui.test_button.setText("测试")

    @logger.catch
    def warn(self):
        """
        警告功能
        :return: 无
        """
        while self.window.life:
            if self.window.state or self.window.test:
                QApplication.processEvents()
                now = datetime.now()
                now = timedelta(
                    hours=now.hour,
                    minutes=now.minute,
                    seconds=now.second,
                )
                for class_over_time in self.window.time_config.keys():
                    hours, minutes = map(int, class_over_time.split(":"))
                    if self.window.test or (
                            timedelta()
                            <= now - timedelta(hours=hours, minutes=minutes)
                            <= timedelta(seconds=self.window.hold_time)
                    ):
                        # 如果差小于持续时间
                        self.window.ui.test_button.setDisabled(True)
                        self.window.ui.test_button.setText("执行中, 请稍候...")
                        logger.debug("执行清剿函数")
                        self.warning_action()
                        break
            sleep(1)
        sys.exit(0)


# region 一些基础类


class GetInput(QWidget):
    """
    自定义获取输入窗口类
    """

    @logger.catch
    def __init__(self, parent: MainWindow, list_widget: QListWidget):
        super().__init__()
        self.ui = get_input.Ui_get_input()
        self.ui.setupUi(self)
        self.connect_window = parent
        self.list_widget = list_widget
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(self.connect_window.tray_icon.files[3]))
        self.hide()

    @logger.catch
    def changeEvent(self, event, /):
        if not self.isActiveWindow():
            self.hide()
        super().changeEvent(event)

    @logger.catch
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.window_pos = self.frameGeometry().topLeft()
            self.drag = True

    @logger.catch
    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    @logger.catch
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag = False


class AddItem(GetInput):
    """
    自定义添加项窗口类
    """

    @logger.catch
    def __init__(self, parent, list_widget):
        super().__init__(parent, list_widget)

    @logger.catch
    def remove_item(self):
        """
        删除选中项
        :return:
        """
        QApplication.processEvents()
        try:
            for_remove_item = self.list_widget.currentItem()
            self.list_widget.takeItem(self.list_widget.currentRow())
            logger.debug(f"已删指定项: {for_remove_item.text()}")
            self.connect_window.flash_state_changed()
        except Exception as error:
            logger.warning(f"删除项失败{error}")

    @logger.catch
    def add_item_func(self):
        """
        添加项到列表
        :return:
        """
        QApplication.processEvents()
        self.hide()
        self.list_widget.addItem(self.ui.get_exe_name.text())
        logger.debug(f"已手动添加项: {self.ui.get_exe_name.text()}")
        self.connect_window.flash_state_changed()

    @logger.catch
    def add_item_function(self):
        """
        处理手动添加项
        :return:
        """
        # 显示程序名称输入框
        self.show()
        self.ui.get_exe_name.clear()


class EditItem(GetInput):
    """
    自定义编辑项窗口类
    """

    @logger.catch
    def __init__(self, parent, list_widget):
        super().__init__(parent, list_widget)

    @logger.catch
    def edit_item_function(self):
        """
        处理编辑项
        :return:
        """
        QApplication.processEvents()
        if self.list_widget.currentItem() is not None:
            self.show()
            self.ui.get_exe_name.setText(self.list_widget.currentItem().text())

    @logger.catch
    def edit_item_func(self):
        """
        处理编辑项函数
        :return:
        """
        QApplication.processEvents()
        self.hide()
        current_item = self.list_widget.currentItem()
        self.list_widget.takeItem(self.list_widget.currentRow())
        self.list_widget.addItem(self.ui.get_exe_name.text())
        logger.debug(
            f"已修改项: {current_item.text()} -> {self.ui.get_exe_name.text()}"
        )
        self.connect_window.flash_state_changed()


# endregion


# region 待杀程序编辑功能实现
class AddEXE(AddItem):
    """
    自定义添加待杀程序窗口类
    """

    @logger.catch
    def __init__(self, parent: MainWindow):
        super().__init__(parent, parent.ui.for_kill_list)
        self.connect_window.ui.remove_exe.clicked.connect(self.remove_item)
        self.connect_window.ui.add_exe.clicked.connect(self.add_item_function)
        self.connect_window.ui.choose_exe.clicked.connect(self.add_exe_by_choose_file)
        self.ui.get_exe_name.returnPressed.connect(self.add_item_func)
        self.connect_window.ui.for_kill_list.itemDoubleClicked.connect(
            self.item_double_clicked_action
        )
        self.ui.label.setText("添加待杀程序")

    @logger.catch
    def add_exe_by_choose_file(self):
        """
        通过选择文件添加待杀程序
        :return: 无
        """
        file_name = basename(
            QFileDialog.getOpenFileName(self.connect_window, "选择待杀程序", "", "*.exe")[0]
        )
        if file_name.strip() != "":
            self.connect_window.ui.for_kill_list.addItem(file_name)
            logger.debug(f"已添加待杀程序: {file_name}")
        self.connect_window.flash_state_changed()

    @logger.catch
    def item_double_clicked_action(self):
        """
        双击待杀程序列表项时执行
        :return:
        """
        QApplication.processEvents()
        kill_exe(self.connect_window.ui.for_kill_list.currentItem().text())


class EditEXE(EditItem):
    """
    自定义编辑待杀程序窗口类
    """

    @logger.catch
    def __init__(self, parent: MainWindow):
        super().__init__(parent, parent.ui.for_kill_list)
        self.connect_window.ui.edit_exe_button.clicked.connect(self.edit_item_function)
        self.ui.get_exe_name.returnPressed.connect(self.edit_item_func)
        self.ui.label.setText("重命名待杀程序")



# endregion


# region 待杀窗口标题编辑功能实现
class AddTitle(AddItem):
    """
    自定义添加待关闭窗口标题窗口类
    """

    @logger.catch
    def __init__(self, parent: MainWindow):
        super().__init__(parent, parent.ui.for_close_title)
        self.connect_window.ui.remove_title.clicked.connect(self.remove_item)
        self.connect_window.ui.add_title.clicked.connect(self.add_item_function)
        self.ui.get_exe_name.returnPressed.connect(self.add_item_func)
        self.ui.label.setText("添加待关闭窗口标题")
        self.ui.get_exe_name.setPlaceholderText("请输入窗口标题")

    @logger.catch
    def item_double_clicked_action(self):
        """
        双击待关闭窗口列表项时执行
        :return:
        """
        QApplication.processEvents()
        self.connect_window.window_closer.kill_windows(
            self.connect_window.ui.for_close_title.currentItem().text()
        )


class EditTitle(EditItem):
    """
    自定义编辑待关闭窗口标题窗口类
    """

    @logger.catch
    def __init__(self, parent: MainWindow):
        super().__init__(parent, parent.ui.for_close_title)
        self.ui.label.setText("重命名待关闭窗口标题")
        self.ui.get_exe_name.setPlaceholderText("请输入待杀窗口标题")
        self.connect_window.ui.edit_title_button.clicked.connect(self.edit_item_function)

# endregion
