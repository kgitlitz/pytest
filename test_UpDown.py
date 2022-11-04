import os
import pytest
import boto3
from moto import mock_s3
from botocore.exceptions import ClientError

from boto_3_up_down import s3_create_bucket, s3_upload, s3_download

test_bucket = "kzy334x6"
test_file = "test.txt"
object_name = "33hellox"

@mock_s3 #decorate for mocking
def test_s3(): #called by pytest 

	client = boto3.client('s3', region_name='us-east-1')

	s3_create_bucket(client, test_bucket)
	
	try:
		response = s3_upload(client, test_file, test_bucket, object_name)
		print(f'Upload Response: {response}')
	except ClientError as e:
		print("error: ", e)
		return False

	#s3_download(client, object_name, test_bucket, "test2.txt")

	return True


def test_noop():
	print('no operation')
	return True

