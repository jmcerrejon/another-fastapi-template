import logging
from datetime import datetime
from pathlib import Path


def setup_logging():
    """
    Configures logging for the project.

    Returns:
        logging.Logger: Configured logger instance.
    """
    log_file = f"logs/{datetime.now().strftime('%Y-%m-%d')}.log"

    Path(log_file).parent.mkdir(parents=True, exist_ok=True)

    format = "%(asctime)s;%(levelname)s;%(message)s"

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format=format,
        filemode="a",
    )

    logger = logging.getLogger()

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(format))
    logger.addHandler(console_handler)

    return logger


# Initialize the logger
logger = setup_logging()
logger.info("App initialized")
