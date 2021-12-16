from celery import shared_task
from django.conf import settings
import boto3
import csv
import os

extensions_cols = ['"col10"']

@shared_task
def csv_task(filename):
    """
    Read csv from S3 or local storage and sum of col10
    :param filename: name of file(not path)
    :return: float sum of columns
    """

    if(not settings.REMOTE_STORAGE):
        filename = f"{settings.LOCAL_FOLDER}/{filename}"
        file_obj = open(filename, "r")
    else:
        client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name='eu-north-1'
        )#init s3 client to download file
        bucket_name = settings.AWS_STORAGE_BUCKET_NAME
        downloaded_file = f'{settings.LOCAL_FOLDER}/data{str(len(os.listdir(settings.LOCAL_FOLDER))+1)}.csv'
        client.download_file(bucket_name, filename, downloaded_file)
        file_obj = open(downloaded_file, "r")

    reader = csv.reader(file_obj)
    total = 0.0

    for row in reader:
        column = " ".join(row).split(',')[11]
        if(column not in extensions_cols and len(column)>2):
            column = column.replace('"', '')
            float_col = float(column)
            total += float_col

    os.remove(file_obj.name)

    return total