from os import popen
from json import load, dump
from sys import argv
from pathlib import Path, PurePath
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QListWidget, QWidget, QCheckBox
from loguru import logger

from classes.basic_classes.Clock import Clock

__all__ = [
    "current_path",
    "set_window_size",
    "kill_exe",
    "flash_list_widget",
    "map_extra",
    "connect_signals",
]


@logger.catch
def current_path(relative_path: str, mode: str = "resource") -> str:
    """
    获取打包后文件资源路径
    :param relative_path: 调试环境路径
    :param mode: 模式, 可选"resource"或"exe", 默认为"resource"
    :return: 无
    """
    QApplication.processEvents()
    match mode:
        case "resource":
            return PurePath.joinpath(
                Path(__file__).resolve().parent, relative_path
            ).__str__()
        case "exe":
            return PurePath.joinpath(
                Path(argv[0]).resolve().parent, relative_path
            ).__str__()
    raise ValueError(f"mode must be 'resource' or 'exe', not {mode}")


@logger.catch
def set_window_size(window: QWidget, application: QApplication):
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
    window.setGeometry(
        width >> 2,
        height >> 2,
        width >> 1,
        height >> 1,
    )


# noinspection SpellCheckingInspection
@logger.catch
def kill_exe(process: str) -> bool:
    """
    根据映像名杀死指定进程
    :param process: 进程映像名
    :return: 是否成功杀死进程
    """
    if (
        process
        == popen(f'tasklist /nh /fi "IMAGENAME eq {process}"')
        .read()
        .split("\n")[1]
        .split("  ")[0]
    ):
        logger.debug(f"杀死进程{process}")
        popen(f"taskkill /f /im {process}")
        return True
    else:
        logger.warning(f"{process}未运行")
        return False


@logger.catch
def flash_list_widget(list_widget: QListWidget) -> list:
    """
    排序所传入的列表控件, 并返回所有项的列表
    :param list_widget: 传入的QListWidget对象
    :return:
    """
    if type(list_widget) != QListWidget:
        raise TypeError("list_widget must be QListWidget")
    list_widget.sortItems()
    return [list_widget.item(i).text() for i in range(list_widget.count())]


# noinspection PyShadowingBuiltins
@logger.catch
def map_extra(func, iterable: list):
    """
    对可迭代对象中的每个元素应用指定函数, 并返回结果列表
    :param func: 要应用的函数
    :param iterable: 可迭代对象
    :return: 结果列表
    """
    return (func(item) for item in iterable)


@logger.catch
def connect_signals(widgets: list, func) -> list:
    """
    连接QObject对象的信号到指定函数
    :param widgets: QObject对象列表
    :param func: 要连接的函数
    :return: 连接结果列表
    """
    return [
        (
            widget.stateChanged.connect(func)
            if type(widget) == QCheckBox
            else widget.valueChanged.connect(func)
        )
        for widget in widgets
    ]


@logger.catch
def load_from_json(file: str) -> dict:
    """
    从JSON文件加载数据
    :param file: JSON文件路径
    :return: 加载的数据字典
    """
    f = open(file=file, mode="r", encoding="utf-8")
    try:
        config: list = load(fp=f)["config"]
        f.close()
        if type(config) == dict:
            return config
        logger.error("加载JSON文件时出错: 数据格式不正确, 预期为字典")
        return {}
    except Exception as e:
        logger.error(f"加载JSON文件时出错: {e}")
        return {}

@logger.catch
def save_to_json(file: str, data: list[list[Clock]]) -> None:
    """
    将数据保存到JSON文件
    :param file: JSON文件路径
    :param data: 要保存的数据字典
    :return: None
    """
    l: list = []
    for day in range(7):
        temp: list = []
        temp.extend([item.time, item.description, item.state] for item in data[day])
        l.append(temp)
    with open(file=file, mode="w", encoding="utf-8") as f:
        dump(obj={"config": l}, fp=f, ensure_ascii=False, indent=4)