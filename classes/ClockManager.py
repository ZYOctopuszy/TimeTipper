if __name__ == "__main__":
    from MainWindow import MainWindow


import bisect
from multiprocessing.spawn import prepare
from PySide6.QtCore import QObject, QTime, Qt
from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtGui import QCursor, QIcon, QMouseEvent
from loguru import logger
import contextlib

from classes.basic_classes.Clock import Clock
from public_functions import save_time_to_json
from .Time import Time


class ClockManager(QObject):
    """
    管理时间点的增删改查
    """

    def __init__(self, p_window: "MainWindow", time_list: QListWidget, day: int):
        super().__init__()
        self.p_window = p_window
        self.day = day
        self.time_list = time_list
        self.day_widget = self.p_window.ui.day
        self.add_time = Time(use_to="add_time")
        self.edit_time = Time(use_to="edit_time")

        # region 连接信号
        self.p_window.ui.add_button.clicked.connect(
            lambda: self.add_time.show()
            and self.add_time.ui.timeEdit.setTime(QTime.currentTime())
        )

        self.p_window.ui.edit_button.clicked.connect(self.edit_button_action)
        self.p_window.ui.delete_button.clicked.connect(self.delete_button_action)

        self.add_time.ui.sure.clicked.connect(self.add_time_action)
        self.edit_time.ui.sure.clicked.connect(self.edit_time_action)

        self.time_list.currentRowChanged.connect(self.update_description)
        self.p_window.ui.description.textChanged.connect(self.change_description)

        self.day_widget.currentIndexChanged.connect(self.reload_time)

        self.p_window.ui.all_disable.clicked.connect(
            lambda: self.change_all(state=False)
        )
        self.p_window.ui.all_enable.clicked.connect(lambda: self.change_all(state=True))
        # endregion

        self.reload_time(self.day)
        self.time_list.viewport().installEventFilter(self)

    @logger.catch
    def eventFilter(self, watched: QObject, event: QMouseEvent) -> bool:
        """
        处理鼠标事件, 右键单击时间点启用/禁用
        """
        if event.type() == QMouseEvent.Type.MouseButtonPress:
            if item := self.time_list.itemAt(
                self.time_list.viewport().mapFromGlobal(QCursor.pos())
            ):
                if event.button() == Qt.MouseButton.RightButton:
                    row = self.time_list.row(item)
                    self.p_window.time_config[self.day_widget.currentIndex()][
                        row
                    ].state ^= True
                    item.setIcon(
                        QIcon(
                            self.p_window.img_files[
                                (
                                    0
                                    if self.p_window.time_config[
                                        self.day_widget.currentIndex()
                                    ][row].state
                                    else 1
                                )
                            ]
                        )
                    )
                self.update_time_config()
            else:
                self.time_list.setCurrentRow(-1)
        return super().eventFilter(watched, event)

    @logger.catch
    def reload_time(self, index: int):
        """
        重新加载时间列表
        :param index: 选中的天数
        :return: 无
        """
        self.time_list.clear()
        self.time_list.addItems(
            [clock.time for clock in self.p_window.time_config[index]]
        )
        for i in range(self.time_list.count()):
            self.time_list.item(i).setIcon(
                QIcon(
                    self.p_window.img_files[
                        (0 if self.p_window.time_config[index][i].state else 1)
                    ]
                )
            )

    @logger.catch
    def change_all(self, state: bool):
        """
        启用或禁用所有时间
        :param state: 是否启用
        :return: 无
        """
        if time_list := self.p_window.time_config[self.day_widget.currentIndex()]:
            for clock in time_list:
                clock.state = state
            for i in range(self.time_list.count()):
                self.time_list.item(i).setIcon(
                    QIcon(self.p_window.img_files[0 if state else 1])
                )
            self.update_time_config()

    @logger.catch
    def edit_button_action(self):
        """
        编辑按钮的槽函数
        :return: 无
        """
        if type(current_item := self.time_list.currentItem()) is QListWidgetItem:
            self.edit_time.ui.timeEdit.setTime(
                QTime.fromString(current_item.text(), "HH:mm")
            )
            self.edit_time.show()

    @logger.catch
    def edit_time_action(self):
        """
        编辑时间
        :return: 无
        """
        self.edit_time.hide()
        before_time: QListWidgetItem = self.time_list.currentItem()
        if (new_time := self.edit_time.ui.timeEdit.time().toString("HH:mm")) not in [
            clock.time
            for clock in self.p_window.time_config[self.day_widget.currentIndex()]
        ]:
            before_time.setText(new_time)
            self.p_window.time_config[self.day_widget.currentIndex()][
                self.time_list.row(before_time)
            ].time = new_time

    @logger.catch
    def add_time_action(self):
        """
        添加时间
        :return: 无
        """
        self.add_time.hide()
        if (new_time := self.add_time.ui.timeEdit.time().toString("HH:mm")) not in [
            clock.time
            for clock in self.p_window.time_config[self.day_widget.currentIndex()]
        ]:

            clocks = self.p_window.time_config[self.day_widget.currentIndex()]
            bisect.insort(a=clocks, x=Clock(time=new_time), key=lambda x: x.time)
            index: int = bisect.bisect_left([c.time for c in clocks], new_time)
            self.time_list.insertItem(index, new_time)
            self.time_list.item(index).setIcon(QIcon(self.p_window.img_files[0]))
            self.update_time_config()

    @logger.catch
    def delete_button_action(self):
        """
        删除按钮的槽函数
        :return: 无
        """
        if type(current_item := self.time_list.currentItem()) is QListWidgetItem:
            current_row = self.time_list.row(current_item)
            self.time_list.takeItem(current_row)
            del self.p_window.time_config[self.day_widget.currentIndex()][current_row]
            self.change_description()

    @logger.catch
    def update_description(self, row: int):
        """
        显示描述
        :return: 无
        """
        if type(current_item := self.time_list.item(row)) is QListWidgetItem:
            self.p_window.ui.description.setPlainText(
                self.p_window.time_config[self.day_widget.currentIndex()][
                    row
                ].description
            )
        else:
            self.p_window.ui.description.clear()

    @logger.catch
    def change_description(self):
        """
        更新描述
        :return: 无
        """
        if type(current_item := self.time_list.currentItem()) is QListWidgetItem:
            self.p_window.time_config[self.day_widget.currentIndex()][
                self.time_list.row(current_item)
            ].description = self.p_window.ui.description.toPlainText()
        self.update_time_config()

    @logger.catch
    def update_time_config(self):
        """
        更新时间配置
        :return: 无
        """
        self.p_window.time_config[self.day_widget.currentIndex()].sort(
            key=lambda clock: clock.time
        )
        save_time_to_json(
            self.p_window.time_config_path, data=self.p_window.time_config
        )
