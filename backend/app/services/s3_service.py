import boto3
from botocore.exceptions import BotoCoreError, ClientError
from app.config.aws_config import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    AWS_BUCKET_NAME,
)
from app.config.logging_config import setup_logging
app_logger, _ = setup_logging()

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    )

def upload_file_to_s3(file_obj, filename, folder="story_images"):
    # Upload file_obj (werkzeug FileStorage) lên S3, trả về URL nếu thành công, None nếu lỗi.
    app_logger.info(f"Bắt đầu upload file: {filename} lên S3, folder: {folder}")
    s3_client = get_s3_client()
    key = f"{folder}/{filename}"
    app_logger.info(f"S3 key: {key}")
    try:
        s3_client.upload_fileobj(
            file_obj,
            AWS_BUCKET_NAME,
            key
        )
        url = f"https://{AWS_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{key}"
        app_logger.info(f"Upload file thành công: {url}")
        return url
    except (BotoCoreError, ClientError) as e:
        app_logger.error(f"Lỗi khi upload file lên S3: {e}")
        return None
