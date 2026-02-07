from collections.abc import Iterable
import win32con, win32gui
from loguru import logger

success: bool
_titles: Iterable[str]


@logger.catch
def kill_windows(titles: Iterable[str]) -> bool:
    """
    关闭所有匹配标题的窗口
    :param titles: 窗口标题
    """
    global success, _titles
    _titles = titles
    success = False
    win32gui.EnumWindows(callback, "")
    return success

@logger.catch
def callback(hwnd: int, *args, **kwargs):
    """
    枚举窗口回调函数，用于查找匹配标题的窗口
    :param hwnd: 窗口句柄
    :param extra: 窗口标题包含的字符串
    """
    global success, _titles
    window_title = win32gui.GetWindowText(hwnd).lower()
    if (
        any(title in window_title for title in _titles)
        and win32gui.IsWindow(hwnd)
        and win32gui.IsWindowVisible(hwnd)
        and win32gui.IsWindowEnabled(hwnd)
    ):
        logger.debug(f"找到匹配窗口 - 句柄: {hwnd}, 标题: {window_title}")
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE)
        success = True


if __name__ == "__main__":
    logger.debug(kill_windows(titles=["for_kill_title"]))
