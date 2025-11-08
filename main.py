from sys import argv
from classes import *

# 创建日志文件
logger.add(
    sink=f"{os.path.dirname(__file__)}\\TimeTipper.log",
    rotation="1024 MB",
    retention="2days",
    encoding="utf-8",
)


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow(app)
    window.setWindowTitle("那刻夏")
    set_window_size(window, app)
    window.thread.start()
    sys.exit(app.exec())
