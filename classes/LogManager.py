if __name__ == "__main__":
    from main_class import MainWindow
from PySide6.QtCore import QObject, Signal
from loguru import logger
import re

_COLOR_TEMPLATE: str = (
    "<font color='{}' face='Cascadia Mono', 'Cascadia Code', 'Microsoft YaHei'>{}</font>"
)
_trans_table = str.maketrans({"<": "&lt;", ">": "&gt;", " ": "&nbsp;"})


class LogManager(QObject):
    update_log = Signal(str)

    @logger.catch
    def __init__(self, p_window: "MainWindow"):
        super().__init__()
        self.p_window = p_window
        self.p_window.ui.logger.clear()
        self.update_log.connect(self.p_window.ui.logger.append)
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
        self.log_pattern = re.compile(
            pattern=r"(.+?) \| (.+?) \| (.+?) -> (.+?) -> (.+?) >>> (.+)"
        )

    @logger.catch
    def write(self, message: str):
        """
        写入日志
        :param message: 日志内容
        :return:
        """
        message_list = message.splitlines()
        if match := self.log_pattern.match(message_list[0]):
            time, level, file, function, line, message = match.groups()
            context = (
                self.become_colorful(text=time, color="green")
                + self.gun  # 时间
                + self.become_colorful(
                    text=level,
                    color=(
                        "blue"
                        if level == "DEBUG"
                        else "yellow" if level == "WARNING" else "red"
                    ),
                )
                + self.gun  # 日志等级
                + self.become_colorful(text=file, color="orange")
                + self.curser  # 文件名
                + self.become_colorful(text=function, color="orange")
                + self.curser  # 函数名
                + self.become_colorful(text=line, color="orange")
                + self.three_cursers  # 行号
                + self.become_colorful(text=message, color="cyan")
            )

            if len(message_list) > 1:
                for line in message_list[1:]:
                    context += "\n<br>" + self.become_colorful(
                        text=line.translate(_trans_table)
                    )

            self.update_log.emit(context)

    @logger.catch
    def become_colorful(self, text: str, color: str = "red") -> str:
        """
        将文本转换为指定颜色的字体
        :param text: 要转换的文本
        :param color: 字体颜色
        :return: 转换后的文本
        """
        return _COLOR_TEMPLATE.format(color, text)
