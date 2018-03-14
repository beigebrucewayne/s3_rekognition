import boto3


s3 = boto3.client('s3')
s3r = boto3.resource('s3')
rek = boto3.client('rekognition')
