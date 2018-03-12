# S3 Rekognition
Detect attributes of images in S3 using AWS Rekognition API. Then, returns data
as Pandas dataframe with easy transfer back to S3.

![banner](https://i.imgur.com/kZHOepy.png)

## Installation

```bash
pip install git+https://github.com/beigebrucewayne/s3_rekognition.git
```

## Usage

```python
from s3_rekognition import login, S3_Rekognition

login = ('AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'REGION')

s3rek = S3_Rekognition()

# See all buckets
s3rek.buckets

# See all files in bucket
s3rek.bucket_content('bucket_name')

# Set filename
s3rek.file = 'filename.jpg'

# Get labels
dataframe = s3rek.get_labels('bucket_name', 'filename')

# Write out to S3
s3rek.to_s3('bucketname', dataframe)
```

## Helpers

Has additional methods to upload and download files.

```python
from s3_rekognition import upload, download

move_files = S3_Rekognition()

move_files.upload('bucket', 'key', 'file')

move_files.download('bucket', 'key', 'file')
```

## Docker

You can test out the package from the Dockerfile, which includes the aws-shell.

```bash
# You'll need the aws-shell before you can use the package
aws-shell

# Should see the following prompt
aws>

# Set up creds + region
aws> configure
```
