import logging
from datetime import datetime
from pathlib import Path


# Module-level references so the file handler is not garbage collected while its
# file handle is still open, and so it can be closed when it gets replaced.
_file_handler: logging.Handler | None = None
_console_handler: logging.Handler | None = None


def setup_logging() -> logging.Logger:
    """
    Configures logging for the project.

    Repeated calls replace the handlers installed by the previous call, closing
    the file handler so its file handle is not leaked.

    Returns:
        logging.Logger: Configured logger instance.
    """
    global _file_handler, _console_handler

    log_file = f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"

    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    format = "%(asctime)s;%(levelname)s;%(message)s"

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    for handler in (_file_handler, _console_handler):
        if handler is not None:
            logger.removeHandler(handler)
            handler.close()

    _file_handler = logging.FileHandler(log_file, mode="a")
    _file_handler.setFormatter(logging.Formatter(format))
    logger.addHandler(_file_handler)

    _console_handler = logging.StreamHandler()
    _console_handler.setFormatter(logging.Formatter(format))
    logger.addHandler(_console_handler)

    return logger


# Initialize the logger
logger = setup_logging()
logger.info("Logger initialized")
