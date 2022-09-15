import logging
import boto3
import json
from botocore.exceptions import ClientError
def handler(event, context):
    s3 = boto3.resource('s3', region_name='us-east-1')
    s3.create_bucket(Bucket='bucket-name')
    content="File uploaded by version 1"
    responses3 = s3.Object('object-name', 'version1.txt').put(Body=content)
    print("uploading file completed")
