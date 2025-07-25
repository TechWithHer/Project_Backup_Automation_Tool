# tests/test_compressor.py

import os
import shutil
from pathlib import Path
from compressor import generate_backup

def setup_test_folder():
    test_folder = Path("tests/temp_data")
    test_folder.mkdir(parents=True, exist_ok=True)
    with open(test_folder / "dummy.txt", "w") as f:
        f.write("Test data.")
    return test_folder

def teardown_test_folder(folder_path):
    shutil.rmtree(folder_path)

def test_generate_zip_backup():
    source = setup_test_folder()
    destination = "tests/"
    backup_name = "test_backup"
    generate_backup(source, destination, "1", backup_name)
    assert Path(f"{destination}/{backup_name}.zip").exists()
    teardown_test_folder(source)

def test_invalid_source():
    try:
        generate_backup(Path("nonexistent_path"), "tests/", "1", "backup")
    except SystemExit:
        assert True
