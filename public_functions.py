"""
公共函数模块, 包含一些通用的函数
"""
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from MainWindow import MainWindow
    from PySide6.QtWidgets import QApplication
from json import dump
from sys import argv
from pathlib import Path, PurePath
from collections.abc import Iterable
from loguru import logger
from itertools import repeat
import psutil
import os

from classes.basic_classes.Clock import Clock

__all__ = [
    "current_path",
    "set_window_size",
    "kill_exes",
    "load_time_from_json",
    "save_time_to_json",
    "time_config",
    "time_class_config",
    "set_window_recordable",
]

@logger.catch
def set_window_recordable(window: MainWindow, recordable: bool = True):
    """
    设置窗口是否可被录屏
    """
    import ctypes
    user32 = ctypes.windll.user32
    hwnd = window.winId()
    match recordable:
        case True:
            user32.SetWindowDisplayAffinity(hwnd, 0x00000000)
        case False:
            user32.SetWindowDisplayAffinity(hwnd, 0x00000011)
    
@logger.catch
def logger_init():
    from sys import stdout
    logger.remove()
    # 创建日志文件
    logger.add(
        sink=current_path(relative_path="TimeTipper.log", mode="exe"),
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | <level>{level}</level> | {name} -> {function} -> {line} >>> {message}",
        rotation="256 KB",
        retention="2 days",
        encoding="utf-8",
        compression="tar.gz",
        enqueue=True,
        backtrace=True,
        catch=True,
    )
    if hasattr(stdout, "closed") and hasattr(stdout, "isatty"):
        # 创建控制台输出
        logger.add(
            sink=stdout,
            format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> <red>|</red> <level>{level}</level> <red>|</red> "
            "<yellow>{name}</yellow> <red>-></red> <yellow>{function}</yellow> <red>-></red> "
            "<yellow>{line}</yellow><red> >>> </red><cyan>{message}</cyan>",
            enqueue=True,
            backtrace=True,
            catch=True,
            colorize=True,
        )


@logger.catch
def get_elevationated_token():
    logger.info("获取管理员权限")
    import winreg, sys
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\ms-settings\shell\open\command")
    command: str = ""
    if argv[0].endswith(".exe"):
        # command = f"{Path(argv[0]).absolute()}"
        command = "C:\\Windows\\System32\\cmd.exe"
    else:
        command = f"{sys.executable} {Path(argv[0]).absolute()}"
    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, command)
    winreg.SetValueEx(key, "DelegateExecute", 0, winreg.REG_SZ, "")
    key.Close()
    import subprocess
    subprocess.run(["fodhelper"])


@logger.catch
def run_as_UIaccess():
    import ctypes, sys
    from ctypes import wintypes
    uiaccess = ctypes.WinDLL('./libs/uiaccess.dll', use_last_error=True)

    # 判断是否已经是uiaccess权限
    if uiaccess.IsUIAccess():
        return

    IsProcessElevated = uiaccess.IsProcessElevated
    IsProcessElevated.argtypes = [wintypes.HANDLE]
    IsProcessElevated.restype = wintypes.BOOL

    StartUIAccessProcess = uiaccess.StartUIAccessProcess
    StartUIAccessProcess.argtypes = [
        wintypes.LPCWSTR,  # lpApplicationName
        wintypes.LPCWSTR,  # lpCommandLine
        wintypes.DWORD,  # flag
        ctypes.POINTER(wintypes.DWORD),  # pPid
        wintypes.DWORD,  # dwSession
    ]
    StartUIAccessProcess.restype = wintypes.BOOL

    # GetLastError = ctypes.windll.kernel32.GetLastError
    # GetLastError.restype = wintypes.DWORD

    def get_current_session_id():
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

        # 定义函数原型
        GetCurrentProcessId = kernel32.GetCurrentProcessId
        GetCurrentProcessId.argtypes = []
        GetCurrentProcessId.restype = wintypes.DWORD

        ProcessIdToSessionId = kernel32.ProcessIdToSessionId
        ProcessIdToSessionId.argtypes = [wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
        ProcessIdToSessionId.restype = wintypes.BOOL

        # 获取当前进程ID
        pid = GetCurrentProcessId()

        # 获取会话ID
        session_id = wintypes.DWORD(0)
        if not ProcessIdToSessionId(pid, ctypes.byref(session_id)):
            raise ctypes.WinError(ctypes.get_last_error())

        return session_id.value

    # 检查管理员权限 (INVALID_HANDLE_VALUE = -1 表示当前进程)
    if not IsProcessElevated(wintypes.HANDLE(-1)):
        get_elevationated_token()
        return False

    # 准备参数
    app_name = None  # 设为NULL
    flag = 0  # 默认标志
    pid = wintypes.DWORD(0)
    session_id = get_current_session_id()  # 当前会话

    # 调用StartUIAccessProcess
    cmd_line = argv[0]
    # logger.debug(cmd_line)
    # logger.debug(Path(cmd_line).resolve())
    if cmd_line.endswith(".exe"):
        cmd_line = f'"{cmd_line}"'
    else:
        logger.debug("不是可执行文件, 无法提升权限")
        return False
    success = StartUIAccessProcess(
        app_name, cmd_line, flag, ctypes.byref(pid), session_id
    )
    if not success:
        logger.error(f"失败: {ctypes.WinError(ctypes.get_last_error())}")
    sys.exit(0 if success else 1)

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
            if argv[0].endswith(".exe"):
                return str(Path(os.environ["APPDATA"]) / "TimeTipper" / relative_path)
            return str(PurePath.joinpath(Path(argv[0]).resolve().parent, relative_path))
        case _:
            raise ValueError(f"mode must be 'resource' or 'exe', not {mode}")


@logger.catch
def set_window_size(window: "MainWindow", application: "QApplication") -> None:
    """
    将窗口居中于屏幕并设置为屏幕尺寸的一半
    :param application: Qt应用对象
    :param window: 要设置的窗口
    :return:
    """
    from PySide6.QtCore import QRect
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
    :param processes: 进程映像名列表（不区分大小写）
    :return: 是否成功杀死进程
    """
    if not processes:
        return False 
    for_kill_processes = [
        proc for proc in psutil.process_iter(['name']) if (proc.info['name'].lower() in [i.lower() for i in processes])
    ]
    if not for_kill_processes:
        # logger.debug("未找到匹配进程")
        return False
    for proc in for_kill_processes:
        proc.kill()
        # logger.debug(f"杀死进程 {proc.name()}")
    return True


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
        from json import load
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


@logger.catch
def save_config(file_name: str, data: dict):
    """
    保存字典数据到json文件
    :param file_name: 文件名
    :param data: 要保存的数据字典
    :return: None
    """
    with open(file=file_name, mode="w", encoding="utf-8") as f:
        dump(obj=data, fp=f, indent=4)
