"""
    Load-Test settings
"""
# python imports
from os import path

# local imports
from .base import *

DEBUG = False

# for s3 bucket
DEFAULT_FILE_STORAGE = 'apps.utility.storage_backend.CustomFileStorage'
