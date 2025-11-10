"""
日志模块测试
"""

import logging
import os
import tempfile
from pathlib import Path

import pytest

from src.logging import get_logger, setup_logging, LogConfig, configure_module_logger


def test_get_logger():
    """测试获取 logger"""
    logger = get_logger("test_logger")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger"


def test_default_logger():
    """测试默认 logger"""
    logger = get_logger()
    assert isinstance(logger, logging.Logger)
    assert logger.name == "algo-models"


def test_log_config():
    """测试日志配置"""
    config = LogConfig(
        name="test_config",
        level="DEBUG",
        format="%(levelname)s - %(message)s",
        log_dir="logs",
        console_output=True,
        file_output=False,
    )

    assert config.name == "test_config"
    assert config.level == "DEBUG"
    assert config.console_output is True
    assert config.file_output is False


def test_setup_logging_console_only():
    """测试仅控制台输出"""
    config = LogConfig(
        name="console_test", level="INFO", console_output=True, file_output=False
    )

    logger = setup_logging(config)
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)


def test_configure_module_logger():
    """测试模块 logger 配置"""
    with tempfile.TemporaryDirectory() as tmpdir:
        logger = configure_module_logger(
            module_name="test_module",
            level="DEBUG",
            log_dir=tmpdir,
            console_output=True,
            file_output=True,
        )

        assert logger.name == "test_module"
        assert logger.level == logging.DEBUG

        log_file = Path(tmpdir) / "test_module.log"
        logger.info("Test message")
        assert log_file.exists()


def test_log_levels():
    """测试不同日志级别"""
    with tempfile.TemporaryDirectory() as tmpdir:
        config = LogConfig(
            name="level_test",
            level="WARNING",
            log_dir=tmpdir,
            log_file="test.log",
            console_output=False,
            file_output=True,
        )

        logger = setup_logging(config)

        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")
        logger.error("error message")

        log_file = Path(tmpdir) / "test.log"
        content = log_file.read_text()

        assert "debug message" not in content
        assert "info message" not in content
        assert "warning message" in content
        assert "error message" in content


def test_multiple_loggers():
    """测试多个独立的 logger"""
    logger1 = get_logger("logger1")
    logger2 = get_logger("logger2")

    assert logger1.name == "logger1"
    assert logger2.name == "logger2"
    assert logger1 is not logger2
