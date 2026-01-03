if __name__ == "__main__":
    from main_class import MainWindow
from json import dump

from PySide6.QtCore import QTime, Qt, QEvent, QObject
from PySide6.QtGui import QIcon, QCursor
from PySide6.QtWidgets import QApplication, QListWidgetItem
from loguru import logger

import classes


class TimeManager(QObject):
    """
    管理时间列表
    """

    def __init__(self, p_window: "MainWindow"):
        super().__init__()
        self.p_window = p_window
        self.add_time = classes.AddTime(use_to="add_time")
        self.edit_time = classes.AddTime(use_to="edit_time")

        self.p_window.ui.add_button.clicked.connect(
            lambda: self.add_time.show() and self.add_time.ui.timeEdit.clear()
        )
        self.p_window.ui.edit_button.clicked.connect(self.edit_button_action)
        self.p_window.ui.delete_button.clicked.connect(self.delete_button_action)

        self.add_time.ui.sure.clicked.connect(self.add_button_action)
        self.edit_time.ui.sure.clicked.connect(self.edit_time_function)

        self.p_window.ui.time_list.itemSelectionChanged.connect(self.flash_description)
        self.p_window.ui.description.textChanged.connect(self.edit_description)
        self.p_window.ui.time_list.addItems(
            sorted(clock.time for clock in self.p_window.time_config)
        )
        for i in range(self.p_window.ui.time_list.count()):
            self.p_window.ui.time_list.item(i).setIcon(
                QIcon(
                    self.p_window.files[0 if self.p_window.time_config[i].state else 1]
                )
            )

        self.list_widget = self.p_window.ui.time_list.viewport().installEventFilter(
            self
        )

    def eventFilter(self, source, event):
        if (
            event.type() == QEvent.Type.MouseButtonPress
            and event.button() == Qt.MouseButton.RightButton
        ):
            if item := self.p_window.ui.time_list.itemAt(
                self.p_window.ui.time_list.viewport().mapFromGlobal(QCursor().pos())
            ):
                for clock in self.p_window.time_config:
                    if clock.time == item.text():
                        clock.state ^= True
                        item.setIcon(
                            QIcon(self.p_window.files[0 if clock.state else 1])
                        )
                self.p_window.update()
                logger.debug(f"切换了时间启用状态: {item.text()}")
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
            clock.time for clock in self.p_window.time_config
        ]:
            self.p_window.time_config.append(
                classes.basic_classes.Clock.Clock(added_time)
            )
            self.p_window.time_config.sort(key=lambda x: x.time)
            self.p_window.ui.time_list.clear()
            self.p_window.ui.time_list.addItems(
                sorted(str(clock) for clock in self.p_window.time_config)
            )
            self.edit_description()

    @logger.catch
    def delete_button_action(self):
        """
        删除当前选中项
        :return: 无
        """
        QApplication.processEvents()
        if current_row := self.p_window.ui.time_list.currentRow():
            self.p_window.ui.time_list.takeItem(current_row)
            del self.p_window.time_config[current_row]
            self.flash_time_config()

    @logger.catch
    def edit_button_action(self):
        """
        显示时间编辑框
        :return:
        """
        QApplication.processEvents()
        if (
            type(current_item := self.p_window.ui.time_list.currentItem())
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
        before_time: str = self.p_window.ui.time_list.currentItem().text()
        if (new_time := self.edit_time.ui.timeEdit.time().toString("HH:mm")) not in [
            clock.time for clock in self.p_window.time_config
        ]:
            self.p_window.ui.time_list.currentItem().setText(new_time)
            for clock in self.p_window.time_config:
                if clock.time == before_time:
                    clock.time = new_time
            self.p_window.ui.time_list.sortItems()
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
        if current_item := self.p_window.ui.time_list.currentItem():
            logger.debug(f"当前选中: {current_item.text()}")
            self.p_window.ui.description.setPlainText(
                next(
                    clock.description
                    for clock in self.p_window.time_config
                    if clock.time == current_item.text()
                )
            )

    @logger.catch
    def edit_description(self):
        """
        刷新当前选中项的描述
        :return: 无
        """
        QApplication.processEvents()

        if current_item := self.p_window.ui.time_list.currentItem():
            for clock in self.p_window.time_config:
                if clock.time == current_item.text():
                    clock.description = self.p_window.ui.description.toPlainText()
            self.flash_time_config()

    @logger.catch
    def flash_time_config(self):
        """
        刷新时间表配置
        :return:
        """
        self.p_window.time_config.sort(key=lambda x: x.time)
        logger.debug(f"已刷新时间表配置, 当前配置:{self.p_window.time_config}")
        with open("clock.json", "w", encoding="utf-8") as f:
            dump(
                obj={
                    clock.time: [
                        clock.description,
                        clock.state,
                    ]
                    for clock in self.p_window.time_config
                },
                fp=f,
                ensure_ascii=False,
                indent=4,
            )

    # endregion
