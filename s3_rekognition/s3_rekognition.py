import boto3
from datetime import datetime
import os
import pandas as pd
from io import StringIO


# Initialize AWS resources
s3 = boto3.client('s3')
s3r = boto3.resource('s3')  # Needed to write to S3
rek = boto3.client('rekognition')

# Today's date for filename
today = datetime.today()
day = f"{today.year}-{today.month}-{today.day}"


def login(key_id: str, secret_key: str, region: str):
    # Set environment variables for boto3
    os.environ['AWS_ACCESS_KEY_ID'] = key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = secret_key
    os.environ['REGION'] = region


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


class S3_Rekognition:
    """Run Rekognition on S3 Objects

    """

    def __init__(self):
        self._buckets = s3.list_buckets()
        self.buckets = [bucket['Name'] for bucket in self._buckets['Buckets']]
        self._file = None

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, filename: str):
        # Set filename for appending to final CSV
        if isinstance(filename, str):
            self._file = filename
        else:
            raise ValueError("File needs to be a String of a filename.")

    @staticmethod
    def bucket_content(bucket: str) -> list:
        # List files within an s3 bucket
        content = s3.list_objects(Bucket=bucket)['Contents']
        return [key['Key'] for key in content]

    @staticmethod
    def get_labels(bucket: str, file: str):
        # Generate labels for S3 image
        rek_response = rek.detect_labels(Image={"S3Object":{"Bucket": bucket,
                                                            "Name": file}})
        rek_labels = rek_response['Labels']
        rek_data = pd.DataFrame(rek_labels)
        rek_data['Image'] = file
        rek_data['Date'] = day
        return rek_data

    def to_s3(self, bucket: str, dataframe):
        # Write datafram back to S3 bucket
        # Name will be:
        # year-month-day-image.csv
        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer)
        filename = f"{day}-{self._file}.csv"
        s3r.Object(bucket, filename).put(Body=csv_buffer.getvalue())
