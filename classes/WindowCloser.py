from collections.abc import Iterable
from typing import Any, List
import win32con
import win32gui
from loguru import logger


@logger.catch
def kill_windows(titles: Iterable[str]) -> bool:
    """
    关闭所有匹配标题的窗口
    :param titles: 窗口标题
    """
    if not titles:
        return False

    extra: List[Any] = [titles, False]
    win32gui.EnumWindows(callback, extra)
    return extra[1]


@logger.catch
def callback(hwnd: int, extra: List[Any]):
    """
    枚举窗口回调函数，用于查找匹配标题的窗口
    :param hwnd: 窗口句柄
    :param extra: 第一项为窗口标题列表, 第二项为是否成功关闭任意一个窗口
    """
    try:
        window_title: str = win32gui.GetWindowText(hwnd).lower()
    except:
        return
    if all(
        (
            any((title in window_title) for title in extra[0]),
            win32gui.IsWindow(hwnd),
            win32gui.IsWindowVisible(hwnd),
            win32gui.IsWindowEnabled(hwnd),
        )
    ):
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE)
        extra[1] = True
