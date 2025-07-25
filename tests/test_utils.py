# tests/test_utils.py
from utils import naming_func

def test_custom_name_returned():
    result = naming_func("backup_2025")
    assert result == "backup_2025"

def test_default_name_generated():
    result = naming_func("0")
    assert result.startswith("_backup_") and len(result) > 8
