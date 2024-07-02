import os
import sys
import boto3
from botocore.exceptions import ClientError
from google.cloud import storage

# AWS S3 credentials (configure your AWS credentials here)
AWS_ACCESS_KEY_ID = 'AK***********YVO'
AWS_SECRET_ACCESS_KEY = 'nN**********************6xM'
AWS_REGION_NAME = 'eu-north-1'
S3_BUCKET_NAME = 'sactest2024'

# Google Cloud Storage credentials (configure your GCP credentials here)
GCP_PROJECT_ID = '***********'
GCS_BUCKET_NAME = 'sactest2024'

# Initialize AWS S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION_NAME
)

# Initialize GCP GCS client
gcs_client = storage.Client(project=GCP_PROJECT_ID)

def upload_to_s3(file_path, bucket, key):
    try:
        s3_client.upload_file(file_path, bucket, key)
        print(f"Uploaded {file_path} to AWS S3 bucket: {bucket}")
    except ClientError as e:
        print(f"Failed to upload {file_path} to AWS S3 bucket: {bucket}")
        print(e)

def upload_to_gcs(file_path, bucket_name, blob_name):
    try:
        bucket = gcs_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_path} to GCP GCS bucket: {bucket_name}")
    except Exception as e:
        print(f"Failed to upload {file_path} to GCP GCS bucket: {bucket_name}")
        print(e)

def main(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.svg', '.webp')):
                # Upload images to AWS S3
                upload_to_s3(file_path, S3_BUCKET_NAME, file_name)
            elif file_name.lower().endswith(('.mp3', '.mp4', '.mpeg4', '.wmv', '.3gp', '.webm')):
                # Upload media files to AWS S3
                upload_to_s3(file_path, S3_BUCKET_NAME, file_name)
            elif file_name.lower().endswith(('.doc', '.docx', '.csv', '.pdf')):
                # Upload documents to GCP GCS
                upload_to_gcs(file_path, GCS_BUCKET_NAME, file_name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python solution.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    main(directory)
