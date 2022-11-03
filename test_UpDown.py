import os
import pytest
import boto3
from moto import mock_s3
from botocore.exceptions import ClientError

from boto_3_up_down import s3_create_bucket, s3_upload, s3_download

test_bucket = "kzy334x6"
test_file = "test.txt"
object_name = "33hellox"

@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

@mock_s3 #decorate for mocking
def test_s3(): #called by pytest 

	s3_create_bucket(aws_credentials, test_bucket)
	
	try:
		response = s3_upload(aws_credentials, test_file, test_bucket, object_name)
		print(f'Upload Response: {response}')
	except ClientError as e:
		print("error: ", e)
		return False

	#s3_download('localstack', object_name, test_bucket, "test2.txt")

	return True

def vtest_s3_aws():

	s3_create_bucket('programmer', test_bucket)
	
	try:
		response = s3_upload('programmer', test_file, test_bucket, object_name)
		print(f'Upload Response: {response}')
	except ClientError as e:
		print("error: ", e)
		return False

	s3_download('programmer', object_name, test_bucket, "test2.txt")

	return True

def test_noop():
	print('no operation')
	return True