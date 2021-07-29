"""
Enforces storage strategies.
"""
# third party imports
from storages.backends.s3boto3 import S3Boto3Storage


class CustomFileStorage(S3Boto3Storage):
    """
    Custom storage for s3
    """
    querystring_auth = False
    file_overwrite = False
