import os


Creds = namedtuple('Creds', [
    'aws_key_id',
    'aws_secret_key',
    'aws_region'
])



def login(key_id: str, secret_key: str, region: str):
    # Set environment variables for boto3
    os.environ['AWS_ACCESS_KEY_ID'] = key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = secret_key
    os.environ['REGION'] = region
