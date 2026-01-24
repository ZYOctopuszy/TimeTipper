if __name__ == "__main__":
    from main_class import MainWindow

import bisect
from PySide6.QtCore import QTime, Qt, QEvent, QObject
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtWidgets import QApplication, QListWidgetItem, QListWidget
from loguru import logger

import classes
from public_functions import save_time_to_json


class TimeManager(QObject):
    """
    管理时间列表
    """

    def __init__(self, p_window: "MainWindow", time_list: QListWidget, day: int):
        super().__init__()
        self.p_window = p_window
        self.day = day
        self.time_list = time_list
        self.day_widget = self.p_window.ui.day
        self.add_time = classes.AddTime(use_to="add_time")
        self.edit_time = classes.AddTime(use_to="edit_time")

        self.connect_signals()

        self.time_list.addItems(
            sorted(clock.time for clock in self.p_window.time_config[self.day])
        )
        for i in range(self.time_list.count()):
            self.time_list.item(i).setIcon(
                QIcon(
                    self.p_window.files[
                        0 if self.p_window.time_config[self.day][i].state else 1
                    ]
                )
            )

        self.list_widget = self.time_list.viewport().installEventFilter(self)

    @logger.catch
    def connect_signals(self):
        """
        连接信号
        """
        self.p_window.ui.add_button.clicked.connect(
            lambda: self.add_time.show() and self.add_time.ui.timeEdit.clear()
        )
        self.p_window.ui.edit_button.clicked.connect(self.edit_button_action)
        self.p_window.ui.delete_button.clicked.connect(self.delete_button_action)

        self.add_time.ui.sure.clicked.connect(self.add_button_action)
        self.edit_time.ui.sure.clicked.connect(self.edit_time_function)

        self.time_list.itemSelectionChanged.connect(self.flash_description)
        self.p_window.ui.description.textChanged.connect(self.edit_description)

        self.day_widget.currentIndexChanged.connect(self.reload_time_list)

        self.p_window.ui.all_disable.clicked.connect(self.all_disable)
        self.p_window.ui.all_enable.clicked.connect(self.all_enable)

    @logger.catch
    def all_disable(self):
        """
        禁用所有时间
        """
        if time_list := self.p_window.time_config[self.day_widget.currentIndex()]:
            for index in range(len(time_list)):
                time_list[index].state = False
                if item := self.time_list.item(index):
                    item.setIcon(
                    QIcon(self.p_window.files[1])
                )
            

    @logger.catch
    def all_enable(self):
        """
        启用所有时间
        """
        if time_list := self.p_window.time_config[self.day_widget.currentIndex()]:
            for index in range(len(time_list)):
                time_list[index].state = True
                if item := self.time_list.item(index):
                    item.setIcon(
                    QIcon(self.p_window.files[0])
                )

    @logger.catch
    def reload_time_list(self, index: int):
        """
        重新加载时间列表
        :return: 无
        """
        self.time_list.clear()
        if self.p_window.time_config[index]:
            self.time_list.addItems(
                sorted(clock.time for clock in self.p_window.time_config[index])
            )
            for i in range(self.time_list.count()):
                self.time_list.item(i).setIcon(
                    QIcon(
                        self.p_window.files[
                            0 if self.p_window.time_config[index][i].state else 1
                        ]
                    )
                )

    @logger.catch
    def eventFilter(self, source, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            if item := self.time_list.itemAt(
                self.time_list.viewport().mapFromGlobal(QCursor().pos())
            ):
                if event.button() == Qt.MouseButton.RightButton:
                    for clock in self.p_window.time_config[
                        self.day_widget.currentIndex()
                    ]:
                        if clock.time == item.text():
                            clock.state ^= True
                            item.setIcon(
                                QIcon(self.p_window.files[0 if clock.state else 1])
                            )
                    self.p_window.update()
                    # logger.debug(f"切换了时间启用状态: {item.text()}")
                    self.flash_time_config()
            else:
                self.time_list.clearSelection()
        return super().eventFilter(source, event)

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
        if (added_time := self.add_time.ui.timeEdit.time().toString("HH:mm")) not in [
            clock.time
            for clock in self.p_window.time_config[self.day_widget.currentIndex()]
        ]:
            clocks: list[classes.basic_classes.Clock.Clock] = self.p_window.time_config[
                self.day_widget.currentIndex()
            ]
            bisect.insort(
                a=clocks,
                x=classes.basic_classes.Clock.Clock(time=added_time),
                key=lambda x: x.time,
            )

            index: int = bisect.bisect_left(a=[c.time for c in clocks], x=added_time)
            self.time_list.insertItem(index, added_time)
            self.time_list.item(index).setIcon(QIcon(self.p_window.files[0]))
            self.flash_time_config()

    @logger.catch
    def delete_button_action(self):
        """
        删除当前选中项
        :return: 无
        """
        QApplication.processEvents()
        if (current_row := self.time_list.currentRow()) + 1:
            self.time_list.takeItem(current_row)
            self.p_window.time_config[self.day_widget.currentIndex()].pop(current_row)
            self.flash_description()
            self.flash_time_config()

    @logger.catch
    def edit_button_action(self):
        """
        显示时间编辑框
        :return:
        """
        QApplication.processEvents()
        if type(current_item := self.time_list.currentItem()) is QListWidgetItem:
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
        before_time: str = self.time_list.currentItem().text()
        if (new_time := self.edit_time.ui.timeEdit.time().toString("HH:mm")) not in [
            clock.time
            for clock in self.p_window.time_config[self.day_widget.currentIndex()]
        ]:
            self.time_list.currentItem().setText(new_time)
            for clock in self.p_window.time_config[self.day_widget.currentIndex()]:
                if clock.time == before_time:
                    clock.time = new_time
            self.time_list.sortItems()
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
        if (current_row := self.time_list.currentRow()) + 1:
            # logger.debug(
            #     f"当前选中: 第{current_row}个: {self.time_list.item(current_row).text()}"
            # )
            self.p_window.ui.description.setPlainText(
                self.p_window.time_config[self.day_widget.currentIndex()][
                    current_row
                ].description
            )
        else:
            self.p_window.ui.description.setPlainText("")

    @logger.catch
    def edit_description(self):
        """
        刷新当前选中项的描述
        :return: 无
        """
        QApplication.processEvents()

        if current_item := self.time_list.currentItem():
            for clock in self.p_window.time_config[self.day_widget.currentIndex()]:
                if clock.time == current_item.text():
                    clock.description = self.p_window.ui.description.toPlainText()
            self.flash_time_config()

    @logger.catch
    def flash_time_config(self):
        """
        刷新时间表配置
        :return:
        """
        self.p_window.time_config[self.day_widget.currentIndex()].sort(
            key=lambda x: x.time
        )
        # logger.debug(
        #     f"已刷新时间表配置, 当前配置:{[time.time for time in self.p_window.time_config[self.day_widget.currentIndex()]]}"
        # )
        save_time_to_json(file=self.p_window.clock_json_path, data=self.p_window.time_config)

    # endregion
