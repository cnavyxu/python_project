"""
日志配置和管理模块
"""

import logging
import sys
from pathlib import Path
from typing import Optional
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from dataclasses import dataclass


@dataclass
class LogConfig:
    """日志配置类"""

    name: str = "algo-models"
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format: str = "%Y-%m-%d %H:%M:%S"
    log_dir: Optional[str] = "logs"
    log_file: Optional[str] = None
    console_output: bool = True
    file_output: bool = True
    max_bytes: int = 10 * 1024 * 1024  # 10MB
    backup_count: int = 5
    rotation_type: str = "size"  # 'size' 或 'time'


_loggers = {}


def setup_logging(config: Optional[LogConfig] = None) -> logging.Logger:
    """
    设置日志系统

    Args:
        config: 日志配置对象

    Returns:
        配置好的 Logger 对象
    """
    if config is None:
        config = LogConfig()

    logger = logging.getLogger(config.name)

    if logger.handlers:
        return logger

    log_level = getattr(logging, config.level.upper(), logging.INFO)
    logger.setLevel(log_level)

    formatter = logging.Formatter(config.format, datefmt=config.date_format)

    if config.console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if config.file_output:
        if config.log_dir:
            log_dir_path = Path(config.log_dir)
            log_dir_path.mkdir(parents=True, exist_ok=True)

            if config.log_file is None:
                config.log_file = f"{config.name}.log"

            log_file_path = log_dir_path / config.log_file

            if config.rotation_type == "size":
                file_handler = RotatingFileHandler(
                    log_file_path,
                    maxBytes=config.max_bytes,
                    backupCount=config.backup_count,
                    encoding="utf-8",
                )
            elif config.rotation_type == "time":
                file_handler = TimedRotatingFileHandler(
                    log_file_path,
                    when="midnight",
                    interval=1,
                    backupCount=config.backup_count,
                    encoding="utf-8",
                )
            else:
                file_handler = logging.FileHandler(log_file_path, encoding="utf-8")

            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    logger.propagate = False

    _loggers[config.name] = logger

    return logger


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    获取 Logger 实例

    Args:
        name: Logger 名称，如果为 None 则使用默认名称

    Returns:
        Logger 对象
    """
    if name is None:
        name = "algo-models"

    if name in _loggers:
        return _loggers[name]

    config = LogConfig(name=name)
    return setup_logging(config)


def configure_module_logger(
    module_name: str,
    level: str = "INFO",
    log_dir: Optional[str] = "logs",
    console_output: bool = True,
    file_output: bool = True,
) -> logging.Logger:
    """
    为特定模块配置 Logger

    Args:
        module_name: 模块名称
        level: 日志级别
        log_dir: 日志目录
        console_output: 是否输出到控制台
        file_output: 是否输出到文件

    Returns:
        配置好的 Logger 对象
    """
    config = LogConfig(
        name=module_name,
        level=level,
        log_dir=log_dir,
        log_file=f"{module_name}.log",
        console_output=console_output,
        file_output=file_output,
    )
    return setup_logging(config)


__all__ = [
    "LogConfig",
    "setup_logging",
    "get_logger",
    "configure_module_logger",
]
