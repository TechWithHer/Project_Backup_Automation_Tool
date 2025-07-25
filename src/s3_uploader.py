# src/s3_uploader.py

import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from logger import get_logger

logger = get_logger()

def upload_to_s3(file_path, bucket_name, s3_key, region="ap-southeast-1"):
    try:
        s3_client = boto3.client('s3', region_name=region)
        s3_client.upload_file(file_path, bucket_name, s3_key)
        logger.info(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
        return True
    except FileNotFoundError:
        logger.error(f"The file {file_path} was not found.")
        return False
    except NoCredentialsError:
        logger.error("AWS credentials not available.")
        return False
    except ClientError as e:
        logger.error(f"AWS ClientError: {e}")
        return False
