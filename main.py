"""
TimeTipper - 一个阻止拖堂的小工具
本项目是一个初中生练手写的, 有很多不足
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
from PySide6.QtWidgets import QApplication

from MainWindow import *
from public_functions import logger_init, run_as_UIaccess


logger_init()

run_as_UIaccess()

if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow(app=app)
    sys_exit(app.exec())
