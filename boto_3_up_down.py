import logging
import boto3
from botocore.exceptions import ClientError

def s3_create_bucket(client, bucket_name):
    print("creating ", bucket_name)

    client.create_bucket(Bucket=bucket_name)

    waiter = client.get_waiter('bucket_exists')
    waiter.wait(Bucket=bucket_name)

def s3_upload(client, file_name, bucket, object_name=None):


    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    try:
        response = client.upload_file(file_name, bucket, object_name)

        waiter = client.get_waiter('object_exists')
        waiter.wait(Bucket=bucket, Key=object_name); 
      
    except ClientError as e: 
        logging.error(e)
        return False
    
    return True

def s3_download(profile, object_name, bucket, file_out):
    
    try:
        response = client.download_file(bucket, object_name, file_out)

        print(f'Download Response: {response}')
    except ClientError as e:
        print(e)
        return False
    
    return True
