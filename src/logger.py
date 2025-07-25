# src/logger.py

import logging
from pathlib import Path

def get_logger(name="backup-tool", log_file="backup.log", level=logging.INFO):
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # Avoid adding duplicate handlers

    logger.setLevel(level)

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(log_dir / log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
