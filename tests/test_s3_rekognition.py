from s3_rekognition import *


# login to AWS
login('access_key_id', 'secret_key', 'region')
s3_class = S3_Rekognition()


def test_s3_list_buckets():
    s3_buckets = s3_class.buckets
    assert isinstance(s3_buckets, list)
    assert isinstance(s3_buckets[0], str)


def test_set_filename():
    s3_class.file = 'testing.jpg'
    assert isinstance(s3_class.file, str)
    assert s3_class.file == 'testing.jpg'


def test_files_in_bucket():
    s3_buckets = s3_class.buckets
    bucket = s3_buckets[0]
    files = s3_class.bucket_content(bucket)
    assert isinstance(files, list)
    assert isinstance(files[0], str)
