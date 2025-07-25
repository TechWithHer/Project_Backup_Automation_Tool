# tests/test_logger.py

import logging
from logger import setup_logger

def test_logging_output(caplog):
    setup_logger()
    logger = logging.getLogger("backup-tool")
    
    with caplog.at_level(logging.INFO):
        logger.info("This is a test log")

    assert "This is a test log" in caplog.text
