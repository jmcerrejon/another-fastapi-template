import logging
import os
from datetime import datetime
from unittest.mock import patch

from src.utils.logger import setup_logging


def _clear_root_handlers() -> None:
    # Close the handlers before dropping them, otherwise the file handler's
    # file handle is leaked when it gets garbage collected.
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        handler.close()
    root_logger.handlers = []


def test_setup_logging_creates_log_file():
    with patch("src.utils.logger.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2023, 1, 1)
        _clear_root_handlers()
        setup_logging()
        log_file = "logs/2023-01-01.log"

        assert os.path.exists(log_file)
        os.remove(log_file)


def test_setup_logging_returns_logger_instance():
    logger = setup_logging()
    assert isinstance(logger, logging.Logger)


def test_setup_logging_adds_console_handler():
    logger = setup_logging()
    console_handler = any(
        isinstance(handler, logging.StreamHandler) for handler in logger.handlers
    )
    assert console_handler


def test_logger_logs_info_message():
    with patch("src.utils.logger.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2023, 1, 1)
        _clear_root_handlers()
        logger = setup_logging()
        log_file = "logs/2023-01-01.log"
        logger.info("Test message")
        with open(log_file, "r") as f:
            log_content = f.read()
        assert "Test message" in log_content
        os.remove(log_file)
