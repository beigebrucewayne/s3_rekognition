from .clients import s3


def download(bucket: str, key: str, file: str):
    # Download file from bucket
    # Key and file are the same if file is not in a
    # folder within the bucket
    try:
        s3.download_file(bucket, key, file)
    except Exception as e:
        print(e)
        print(f"Error downloading {file} from {bucket}")
        raise e

def upload(bucket: str, key: str, file: str):
    # Upload file back to S3
    # File and key should be the same,
    # unless you want the file under a different folder
    try:
        s3.upload_file(file, bucket, key)
    except Exception as e:
        print(e)
        print(f"Error uploading {file} to {bucket}")
        raise e
