if __name__ == "__main__":
    from MainWindow import MainWindow
    from .basic_classes.Clock import Clock

from itertools import repeat

from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import QTimer
from datetime import datetime
from loguru import logger

from public_functions import load_time_from_json, time_class_config, time_config
from classes.basic_classes.Clock import Clock

class DayManager:
    """
    日期管理类
    """
    _config_cache: dict[str, time_class_config] = {}

    def __init__(
        self,
        p_window: "MainWindow",
        day_widget: QComboBox,
        time_config: time_class_config,
    ):
        self.p_window = p_window
        self.day_widget = day_widget
        self.time_config = time_config
        self.day: int = datetime.now().isoweekday() - 1
        self.p_window.ui.select_now.clicked.connect(self.set_as_current_day)
        self.set_as_current_day()
        self.time_updater = QTimer()
        self.time_updater.timeout.connect(self.refresh_time)
        self.time_updater.start(1000)

    @logger.catch
    def set_as_current_day(self):
        """
        设置当前日期
        :return: 无
        """
        self.day = datetime.now().isoweekday() - 1
        self.day_widget.setCurrentIndex(self.day)

    @logger.catch
    def refresh_time(self):
        """
        刷新时间显示
        :return: 无
        """
        self.p_window.ui.show_time.setText(
            f"{datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}, {self.day_widget.itemText(self.day)}"
        )


    @logger.catch
    @staticmethod
    def get_time_config(config_json_path: str) -> time_class_config:
        """
        获取时间配置
        :param config_json_path: 配置文件路径
        :return: 时间配置对象
        """
        if config_json_path in DayManager._config_cache:
            return DayManager._config_cache[config_json_path]
        config_list: time_config = load_time_from_json(file=config_json_path)
        result: time_class_config = list(repeat([], 7))
        if len(config_list) != 7:
            logger.error(
                f"加载JSON文件时出错: 数据格式不正确, 预期为7天的列表, 但得到了{len(config_list)}天"
            )
            return result
        for day in range(7):
            for item in config_list[day]:
                if (
                    len(item) == 3
                    and isinstance(item[0], str)
                    and isinstance(item[1], str)
                    and isinstance(item[2], bool)
                ):
                    result[day].append(
                        Clock(time=item[0], description=item[1], state=item[2])
                    )
                else:
                    logger.error(
                        f"加载JSON文件时出错: 数据格式不正确, 预期为[时间, 描述, 状态], 但得到了{item}"
                    )
        DayManager._config_cache[config_json_path] = result
        return result

