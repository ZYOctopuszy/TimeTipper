if __name__ == "__main__":
    from MainWindow import MainWindow
import sys
import threading
from datetime import datetime, timedelta, time
from random import randint
from time import sleep

from loguru import logger

from public_functions import kill_exes


class MessageShower:
    """
    自定义消息显示类
    """

    @logger.catch
    def __init__(self, p_window: "MainWindow"):
        self.p_window = p_window
        self.day = self.p_window.day_manager.day
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
            randint(a=self.p_window.config.random_time[0], b=self.p_window.config.random_time[1])
            if self.p_window.test
            or (
                now.strftime(format="%H:%M")
                in [clock.time for clock in self.p_window.time_config[self.day]]
                and now.second < self.p_window.config.random_time[0]
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
                success = False
                logger.debug("关闭窗口中")
                if self.p_window.config.forKillWindowTitle and any(
                    self.p_window.kill_windows(titles=title)
                    for title in self.p_window.config.forKillWindowTitle
                ):
                    success = True
                logger.debug("杀死进程中")
                if self.p_window.config.forKillExe and kill_exes(
                    processes=self.p_window.config.forKillExe
                ):
                    success = True
                if success:
                    self.p_window.app.beep()
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
            if self.p_window.test or self.p_window.state:
                now = datetime.now()
                current_time = now.time()
                hold_start = now - timedelta(seconds=self.p_window.config.hold_time)

                if self.p_window.test or [
                    (c.hours, c.minutes)
                    for c in self.p_window.time_config[self.day]
                    if c.state
                    and hold_start.time()
                    <= time(hour=c.hours, minute=c.minutes)
                    <= current_time
                ]:
                    self.p_window.ui.test_button.setDisabled(True)
                    self.p_window.ui.test_button.setText("执行中, 请稍候...")
                    logger.debug("执行清剿函数")
                    self.killer()
            sleep(1)
        sys.exit(0)
