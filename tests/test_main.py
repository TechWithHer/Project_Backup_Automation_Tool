# tests/test_main.py

from unittest.mock import patch
from pathlib import Path
import os
from compressor import generate_backup
from utils import naming_func

def test_end_to_end_backup_flow(tmp_path):
    dummy_source = tmp_path / "testdir"
    dummy_source.mkdir()
    (dummy_source / "file.txt").write_text("Sample")

    destination = tmp_path
    file_type = "1"
    backup_name = naming_func("0")

    generate_backup(dummy_source, destination, file_type, backup_name)
    
    backup_file = destination / f"{backup_name}.zip"
    assert backup_file.exists()
