from sys import argv

from classes import *

# 创建日志文件
logger.add(
    sink=f"{os.path.dirname(os.path.abspath(__file__)) if hasattr(sys, "_MEIPASS") else abspath(".")}\\TimeTiper.log",
    rotation="1024 MB",
    retention="2days",
    encoding="utf-8",
)

# region 初始化
app = QApplication(argv)
window = MainWindow(app)
window.setWindowTitle("那刻夏")
set_window_size(window, app)

if __name__ == "__main__":
    window.thread.start()
    sys.exit(app.exec())
