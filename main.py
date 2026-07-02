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

from sys import exit as sys_exit, argv

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

from MainWindow import *
from public_functions import logger_init, run_as_UIaccess


logger_init()

run_as_UIaccess()

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow(app=app)
    sys_exit(app.exec())
