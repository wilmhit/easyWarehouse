from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class S3(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
