# tests/test_s3_uploader.py

import boto3
from moto import mock_s3
from pathlib import Path
from s3_uploader import upload_to_s3  # This is your function

@mock_s3
def test_upload_to_s3_mock():
    # Setup
    bucket_name = "test-backup-bucket"
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=bucket_name)

    # Create dummy file
    file_path = Path("test_backup.zip")
    file_path.write_text("dummy content")

    # Upload
    result = upload_to_s3(str(file_path), bucket_name, "backup/test_backup.zip")
    assert result is True  # If your upload function returns True on success

    # Verify upload
    response = s3.get_object(Bucket=bucket_name, Key="backup/test_backup.zip")
    assert response["Body"].read().decode() == "dummy content"

    # Cleanup
    file_path.unlink()
