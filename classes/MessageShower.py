if __name__ == "__main__":
    from main_class import MainWindow
import sys
import threading
from datetime import datetime, timedelta
from random import randint
from time import sleep

from PySide6.QtWidgets import QSystemTrayIcon, QApplication
from loguru import logger

from public_functions import mapx, kill_exe


class MessageShower:
    """
    自定义消息显示类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow"):
        self.p_window = p_window
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
            randint(self.p_window.random_time[0], self.p_window.random_time[1])
            if now.strftime("%H:%M") in [clock.time for clock in self.p_window.time_config]
            or self.p_window.test
            else 0
        )
        logger.debug(f"将等待时间: {wait_second}秒")
        while self.p_window.life and self.p_window.state:
            if datetime.now() - (now + timedelta(seconds=wait_second)) <= timedelta():
                sleep(1)
                continue
            else:
                logger.debug("关闭窗口中")
                if self.p_window.forKillWindowTitle:
                    mapx(
                        self.p_window.window_closer.kill_windows,
                        self.p_window.forKillWindowTitle,
                    )
                logger.debug("杀死进程中")
                if self.p_window.forKillExe and True in mapx(
                    kill_exe, self.p_window.forKillExe
                ):
                    self.p_window.app.beep()
                break
        self.p_window.test = False
        self.p_window.ui.test_button.setEnabled(True)
        self.p_window.ui.test_button.setText("测试")

    @logger.catch
    def warn(self):
        """
        警告功能
        :return: 无
        """
        while self.p_window.life:
            if self.p_window.state or self.p_window.test:
                QApplication.processEvents()
                now = datetime.now()
                now = timedelta(
                    hours=now.hour,
                    minutes=now.minute,
                    seconds=now.second,
                )
                for class_over_time in (c.time for c in list(self.p_window.time_config) if c.state):
                    hours, minutes = map(int, class_over_time.split(":"))
                    if self.p_window.test or (
                        timedelta()
                        <= now - timedelta(hours=hours, minutes=minutes)
                        <= timedelta(seconds=self.p_window.hold_time)
                    ):
                        # 如果差小于持续时间
                        self.p_window.ui.test_button.setDisabled(True)
                        self.p_window.ui.test_button.setText("执行中, 请稍候...")
                        logger.debug("执行清剿函数")
                        self.warning_action()
                        break
            sleep(1)
        sys.exit(0)
