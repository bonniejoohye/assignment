from .models import Post, Comment
from file_upload.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME
import boto3
from boto3.session import Session
from datetime import datetime
from django.contrib.auth.models import User

# Create your views here.

def upload_and_create(request, file_to_upload):
    #create client
    session = Session(
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
            region_name = AWS_S3_REGION_NAME
    )
    s3 = session.resource('s3')

    #s3 에 file upload

    now = datetime.now().strftime("%Y%H%M%S")
    user_pk = str(request.user.pk) + '/'
    
    try:
        img_object = s3.Bucket(AWS_STORAGE_BUCKET_NAME).put_object(
            Key = now + user_pk + file_to_upload.name,
            Body = file_to_upload
        )
  
        s3_url = 'https://joohye.s3.ap-northeast-2.amazonaws.com/' + now + user_pk + file_to_upload.name
        return s3_url 

    except AttributeError:
        print('사진파일 없음')