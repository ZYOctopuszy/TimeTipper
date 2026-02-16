"""
公共函数模块, 包含一些通用的函数
"""
if __name__ == "__main__":
    from MainWindow import MainWindow
from json import load, dump
from sys import argv
from pathlib import Path, PurePath
from collections.abc import Iterable
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QListWidget
from loguru import logger
from itertools import repeat
import psutil

from classes.basic_classes.Clock import Clock

__all__ = [
    "current_path",
    "set_window_size",
    "kill_exes",
    "flash_list_widget",
    "load_time_from_json",
    "save_time_to_json",
    "time_config",
    "time_class_config",
]


@logger.catch
def current_path(relative_path: str, mode: str = "resource") -> str:
    """
    获取打包后文件资源路径
    :param relative_path: 调试环境路径
    :param mode: 模式, 可选"resource"或"exe", 默认为"resource"
    :return: 无
    """
    match mode:
        case "resource":
            return str(
                PurePath.joinpath(Path(__file__).resolve().parent, relative_path)
            )
        case "exe":
            return str(PurePath.joinpath(Path(argv[0]).resolve().parent, relative_path))
        case _:
            raise ValueError(f"mode must be 'resource' or 'exe', not {mode}")


@logger.catch
def set_window_size(window: "MainWindow", application: QApplication) -> None:
    """
    将窗口居中于屏幕并设置为屏幕尺寸的一半
    :param application: Qt应用对象
    :param window: 要设置的窗口
    :return:
    """
    # 获取屏幕的尺寸
    available_geometry: QRect = application.screens()[0].availableGeometry()
    width = available_geometry.width()
    height = available_geometry.height()

    # 应用窗口位置
    window.ui.main_frame.setGeometry(
        width >> 2,
        height >> 2,
        width >> 1,
        height >> 1,
    )


@logger.catch
def kill_exes(processes: Iterable[str]) -> bool:
    """
    根据映像名杀死指定进程
    :param processes: 进程映像名列表（区分大小写）
    :return: 是否成功杀死进程
    """
    matched_processes: set = (set(psutil.process_iter(attrs=["name"])) & set(processes))
    if not matched_processes:
        logger.debug("未找到匹配进程")
        return False
    for proc in matched_processes:
        proc.kill()
        logger.debug(f"杀死进程 {proc.name()}")
    return True


@logger.catch
def flash_list_widget(list_widget: QListWidget) -> list[str]:
    """
    排序所传入的列表控件, 并返回所有项的列表
    :param list_widget: 传入的QListWidget对象
    :return:
    """
    if type(list_widget) != QListWidget:
        raise TypeError("list_widget must be QListWidget")
    list_widget.sortItems()
    return [list_widget.item(i).text() for i in range(list_widget.count())]


type time_config = list[list[list[str | bool]]]
type time_class_config = list[list[Clock]]

_json_cache: dict[str, time_config] = {}


@logger.catch
def load_time_from_json(file: str) -> time_config:
    """
    从JSON文件加载数据
    :param file: JSON文件路径
    :return: 加载的数据列表
    """
    if file in _json_cache:
        return _json_cache.get(file, [])
    if not Path(file).is_file():
        logger.error(f"文件 {file} 不存在")
        return [[] for _ in repeat(None, 7)]
    with open(file=file, mode="r", encoding="utf-8") as f:
        config: time_config = load(fp=f).get("config", [])
    return config


@logger.catch
def save_time_to_json(file: str, data: time_class_config) -> None:
    """
    将数据保存到JSON文件
    :param file: JSON文件路径
    :param data: 要保存的数据字典
    :return: None
    """
    cfg_L: time_config = []
    for day in range(7):
        temp: list[list[str | bool]] = []
        temp.extend([item.time, item.description, item.state] for item in data[day])
        cfg_L.append(temp)
    with open(file=file, mode="w", encoding="utf-8") as f:
        dump(obj={"config": cfg_L}, fp=f, ensure_ascii=False, indent=4)
    _json_cache[file] = cfg_L
