from sys import exit, argv, stdout

from PySide6.QtWidgets import QApplication
from loguru import logger

from main_classes import *
from public_functions import current_path

# 创建日志文件
logger.remove()
logger.add(
    sink=current_path("TimeTipper.log", "exe"),
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
