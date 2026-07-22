if __name__ == "__main__":
    from MainWindow import MainWindow
import sys
import threading
from datetime import datetime, timedelta
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
        self.thread = threading.Thread(target=self.clock)
        self.thread.start()

    # region 通知提醒功能实现
    @logger.catch
    def killer(self):
        """
        当下课时执行的操作(关闭相关软件!)
        :return:
        """
        now = datetime.now()
        wait_second = (
            randint(
                a=self.p_window.config.random_delay[0],
                b=self.p_window.config.random_delay[1],
            )
            if self.p_window.is_testing
            or (
                now.strftime(format="%H:%M")
                in [clock.time for clock in self.p_window.time_config[self.day]]
                and now.second < self.p_window.config.random_delay[0]
            )
            else 0
        )
        # logger.debug(f"将等待时间: {wait_second}秒")
        while self.p_window.is_alive and (
            self.p_window.is_testing or self.p_window.status
        ):
            if wait_second > 0:
                wait_second -= 1
                sleep(1)
            else:
                try:
                    # logger.debug("关闭窗口中")
                    success: bool = True
                    if not self.p_window.kill_windows(
                        titles=self.p_window.config.for_kill_window_titles
                    ):
                        success = False
                    # logger.debug("杀死进程中")
                    if not kill_exes(processes=self.p_window.config.for_kill_exes):
                        success = False
                    if success:
                        self.p_window.app.beep()
                    break
                except Exception as e:
                    logger.error(e)
        self.p_window.is_testing = False
        self.p_window.ui.test_button.setEnabled(True)
        self.p_window.ui.test_button.setText("测试")

    @logger.catch
    def clock(self):
        """
        警告功能
        :return: 无
        """
        while self.p_window.is_alive:
            if self.p_window.is_testing or self.p_window.status:
                now = datetime.now().replace(microsecond=0)
                current_time = now
                duration_seconds_before = now - timedelta(
                    seconds=self.p_window.config.duration
                )

                # logger.debug(
                #     f"{
                #         duration_seconds_before=}, {
                #         current_time=}, {
                #         self.p_window.time_config[self.day]=}, {[
                #     (c.hours, c.minutes)
                #     for c in self.p_window.time_config[self.day]
                #     if c.state
                #     and duration_seconds_before
                #     <= (target_time := now.replace(hour=c.hours(), minute=c.minutes(), second=0))
                #     <= current_time
                # ]}"
                # )

                if self.p_window.is_testing or [
                    (c.hours, c.minutes)
                    for c in self.p_window.time_config[self.day]
                    if c.state
                    and duration_seconds_before
                    <= datetime.strptime(
                        f"{now.year}-{now.month}-{now.day} {c.hours()}:{c.minutes()}",
                        "%Y-%m-%d %H:%M",
                    )
                    <= current_time
                ]:
                    self.p_window.ui.test_button.setDisabled(True)
                    self.p_window.ui.test_button.setText("执行中, 请稍候...")
                    # logger.debug("执行清剿函数")
                    self.killer()
            sleep(1)
        sys.exit(0)
