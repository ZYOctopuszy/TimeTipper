import win32con, win32gui
from loguru import logger

count: int = 0


@logger.catch
def kill_windows(title: str = "") -> bool:
    """
    关闭所有匹配标题的窗口
    :param title: 窗口标题
    """
    global count
    count = 0
    win32gui.EnumWindows(callback, title)
    return bool(count)


@logger.catch
def callback(hwnd, extra):
    """
    枚举窗口回调函数，用于查找匹配标题的窗口
    :param hwnd: 窗口句柄
    :param extra: 窗口标题包含的字符串
    """
    global count
    window_title = win32gui.GetWindowText(hwnd)
    if extra.lower() in window_title.lower() and win32gui.IsWindow(hwnd):
        logger.debug(f"找到匹配窗口 - 句柄: {hwnd}, 标题: {window_title}")
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE)
        count += 1


if __name__ == "__main__":
    logger.debug(kill_windows(title="for_kill_title"))
