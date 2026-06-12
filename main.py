"""
TimeTipper - 一个时间管理小工具
"""

# region 编译配置
# nuitka-project: --mode=onefile
# nuitka-project: --onefile-no-compression
# nuitka-project: --include-data-dir=icons=icons
# nuitka-project: --output-filename=TimeTipper-latest
# nuitka-project: --output-dir=dist
# nuitka-project: --msvc=latest
# nuitka-project: --remove-output
# nuitka-project: --windows-console-mode=disable
# nuitka-project: --windows-icon-from-ico=icons\active.ico
# nuitka-project: --windows-uac-admin
# nuitka-project: --enable-plugin=pyside6
# nuitka-project: --plugin-enable=upx
# nuitka-project: --lto=yes
# nuitka-project: --show-progress
# endregion

from sys import exit as sys_exit, argv, stdout

# if argv[0].endswith(".exe"):
#     """
#     检查当前进程是否为conhost.exe, 如果不是则复制并启动conhost.exe
#     """
#     import psutil, os, subprocess
#     current_process = psutil.Process(os.getpid())
#     if current_process.name() != "conhost.exe":
#         import shutil, pathlib

#         shutil.copy2(
#             pathlib.Path(argv[0]),
#             pathlib.Path(os.environ["APPDATA"]) / "TimeTipper" / "conhost.exe",
#         )
#         subprocess.Popen(pathlib.Path(os.environ["APPDATA"]) / "TimeTipper" / "conhost.exe")
#         sys_exit(0)
from PySide6.QtWidgets import QApplication
from loguru import logger

from MainWindow import *
from public_functions import current_path, run_as_UIaccess

run_as_UIaccess()

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
    sys_exit(app.exec())
