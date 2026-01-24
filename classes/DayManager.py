if __name__ == "__main__":
    from main_class import MainWindow

from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QTimer

from datetime import datetime
from public_functions import load_time_from_json
from classes.basic_classes.Clock import Clock
from loguru import logger


class DayManager:
    _config_cache = {}

    def __init__(
        self,
        p_window: "MainWindow",
        day_widget: QComboBox,
        time_config: list[list[Clock]],
    ):
        self.p_window = p_window
        self.time_config = time_config
        self.day: int = datetime.now().isoweekday() - 1
        self.day_widget: QComboBox = day_widget
        self.p_window.ui.select_now.clicked.connect(self.set_current_day)
        self.set_current_day()
        self.time_updater = QTimer()
        self.time_updater.timeout.connect(self.flash_date)
        self.time_updater.start(1000)

    @logger.catch
    @staticmethod
    def get_config(config_json: str) -> list:
        """
        获取时间配置
        :param config_json: 时间配置JSON文件路径
        :return: 时间配置列表
        """
        if config_json in DayManager._config_cache:
            return DayManager._config_cache[config_json]
        config_list: list = load_time_from_json(file=config_json)
        result: list = [[], [], [], [], [], [], []]
        if len(config_list) != 7:
            return result
        for day in range(7):
            for item in config_list[day]:
                if (
                    len(item) == 3
                    and type(item[0]) == str
                    and type(item[1]) == str
                    and type(item[2]) == bool
                ):

                    result[day].append(
                        Clock(time=item[0], description=item[1], state=item[2])
                    )
                else:
                    logger.error(
                        f"加载JSON文件时出错: 数据格式不正确, 预期为[时间, 描述, 状态], 但得到了{item}"
                    )
        DayManager._config_cache[config_json] = result
        return result

    @logger.catch
    def set_current_day(self):
        """
        设置为当前日期
        """
        self.day_widget.setCurrentIndex(self.day)

    @logger.catch
    def flash_date(self):
        """
        刷新时间
        """
        datetime.now()
        self.p_window.ui.show_time.setText(
            f"{datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}, {self.day_widget.itemText(self.day)}"
        )
