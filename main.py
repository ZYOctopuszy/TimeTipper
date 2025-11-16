import sys
from sys import stdout, exit, argv

from PySide6.QtWidgets import QApplication
from loguru import logger

from main_classes import *
from public_functions import current_path

# 创建日志文件
logger.remove()
logger.add(
    sink=current_path("TimeTipper.log", "exe"),
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level}</level> | {name} -> {function} -> {line} >>> {message}",
    rotation="1024 MB",
    retention="2days",
    encoding="utf-8",
    compression="zip",
    enqueue=True,
    backtrace=True,
    catch=True,
)
logger.debug("创建了日志文件")
if not hasattr(sys, '_MEIPASS'):
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
    window = MainWindow(app)
    exit(app.exec())
