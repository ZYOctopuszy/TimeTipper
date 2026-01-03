from sys import exit, argv, stdout

from PySide6.QtWidgets import QApplication
from loguru import logger

from main_class import *
from public_functions import current_path

logger.remove()
# 创建日志文件
logger.add(
    sink=current_path(relative_path="TimeTipper.log", mode="exe"),
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level}</level> | {name} -> {function} -> {line} >>> {message}",
    rotation="256 KB",
    retention="2 days",
    encoding="utf-8",
    compression="tar.gz",
    enqueue=True,
    backtrace=True,
    catch=True,
)
if hasattr(stdout, "closed") and hasattr(stdout, "isatty"):
    # 创建控制台输出
    logger.add(
        sink=stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <red>|</red> <level>{level}</level> <red>|</red> "
        "<yellow>{name}</yellow> <red>-></red> <yellow>{function}</yellow> <red>-></red> "
        "<yellow>{line}</yellow><red> >>> </red><cyan>{message}</cyan>",
        enqueue=True,
        backtrace=True,
        catch=True,
        colorize=True,
    )

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow(app=app)
    exit(app.exec())
