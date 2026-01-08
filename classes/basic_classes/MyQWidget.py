from PySide6.QtCore import Qt
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import QEvent, QTimer
from PySide6.QtWidgets import QWidget
from loguru import logger


class MyQWidget(QWidget):
    """
    自定义QWidget类, 用于设置窗口属性
    """

    @logger.catch
    def __init__(self, auto_hide: bool = True):
        super().__init__()
        self.auto_hide = auto_hide
        self.drag = False

    @logger.catch
    def changeEvent(self, event, /):
        if self.auto_hide and not self.isActiveWindow():
            self.hide()
        super().changeEvent(event)

    @logger.catch
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.window_pos = self.pos()
            self.mouse_start_pt = event.globalPosition().toPoint()
            self.drag = True

    @logger.catch
    def mouseMoveEvent(self, event: QMouseEvent):
        if self.drag:
            distance = event.globalPosition().toPoint() - self.mouse_start_pt
            self.move(self.window_pos + distance)

    @logger.catch
    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag = False

    @logger.catch
    def changeEvent(self, event: QEvent):
        """
        处理窗口最小化行为
        :param event: 事件对象
        :return: 无
        """
        if (
            self.windowState() == Qt.WindowState.WindowMinimized
            and event.type() == QEvent.Type.WindowStateChange
        ):
            QTimer.singleShot(0, self.hide)
        super().changeEvent(event)
