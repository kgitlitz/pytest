import logging
import boto3
from botocore.exceptions import ClientError

def s3_create_bucket(profile, bucket_name):
    print("creating ", bucket_name)
    session = boto3.Session(profile_name=profile)
    s3 = session.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=bucket_name)

    waiter = s3.get_waiter('bucket_exists')
    waiter.wait(Bucket=bucket_name)

def s3_upload(profile, file_name, bucket, object_name=None):

    session = boto3.Session(profile_name=profile)


    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    s3 = session.client("s3", region_name="us-east-1")

    try:
        response = s3.upload_file(file_name, bucket, object_name)

        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=bucket, Key=object_name); 
      
    except ClientError as e: 
        logging.error(e)
        return False
    
    return True

def s3_download(profile, object_name, bucket, file_out):

    session = boto3.Session(profile_name=profile)
    
    s3 = session.client("s3", region_name="us-east-1")
    
    try:
        response = s3.download_file(bucket, object_name, file_out)

        print(f'Download Response: {response}')
    except ClientError as e:
        print(e)
        return False
    
    return True

#@mock_s3 #decorate for mocking
#def test_s3(): #called by pytest
 #   s3_create_bucket('localstack', 'kbucket')


#test_s3()