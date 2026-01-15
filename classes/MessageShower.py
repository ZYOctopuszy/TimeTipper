if __name__ == "__main__":
    from main_class import MainWindow
import sys
import threading
from datetime import datetime
from random import randint
from time import sleep

from PySide6.QtWidgets import QApplication
from loguru import logger

from public_functions import map_extra, kill_exe


class MessageShower:
    """
    自定义消息显示类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow"):
        self.p_window = p_window
        threading.Thread(target=self.clock).start()

    # region 通知提醒功能实现
    @logger.catch
    def killer(self):
        """
        当下课时执行的操作(关闭相关软件!)
        :return:
        """
        now = datetime.now()
        wait_second = (
            randint(self.p_window.random_time[0], self.p_window.random_time[1])
            if self.p_window.test
            or (
                now.strftime("%H:%M")
                in [clock.time for clock in self.p_window.time_config]
                and now.second < self.p_window.random_time[0]
            )
            else 0
        )
        logger.debug(f"将等待时间: {wait_second}秒")
        while self.p_window.life and self.p_window.state:
            if wait_second > 0:
                wait_second -= 1
                sleep(1)
                continue
            else:
                logger.debug("关闭窗口中")
                if self.p_window.forKillWindowTitle and True in map_extra(
                    self.p_window.kill_windows,
                    self.p_window.forKillWindowTitle,
                ):
                    # self.p_window.app.beep()
                    ...
                logger.debug("杀死进程中")
                if self.p_window.forKillExe and True in map_extra(
                    kill_exe, self.p_window.forKillExe
                ):
                    ...
                    # self.p_window.app.beep()
                break
        self.p_window.test = False
        self.p_window.ui.test_button.setEnabled(True)
        self.p_window.ui.test_button.setText("测试")

    @logger.catch
    def clock(self):
        """
        警告功能
        :return: 无
        """
        while self.p_window.life:
            if self.p_window.test:
                self.p_window.ui.test_button.setDisabled(True)
                self.p_window.ui.test_button.setText("执行中, 请稍候...")
                logger.debug("执行清剿函数")
                self.killer()
            elif self.p_window.state:
                QApplication.processEvents()
                now = datetime.now()
                for class_over_time in (
                    c for c in self.p_window.time_config if c.state
                ):
                    if (
                        0
                        <= (
                            now
                            - now.replace(
                                hour=class_over_time.hours,
                                minute=class_over_time.minutes,
                                second=0,
                                microsecond=0,
                            )
                        ).total_seconds()
                        <= self.p_window.hold_time
                    ):
                        # 如果差小于持续时间
                        self.p_window.ui.test_button.setDisabled(True)
                        self.p_window.ui.test_button.setText("执行中, 请稍候...")
                        logger.debug("执行清剿函数")
                        self.killer()
                        break
            sleep(1)
        sys.exit(0)
