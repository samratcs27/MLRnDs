
import logging
import pickle

import boto3
from botocore.exceptions import ClientError
import os



class S3Loader:
    upload_files = {}

    @staticmethod
    def upload_file_to_S3(bucket, aws_key, aws_secret, location=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        for file_path,object_name in S3Loader.upload_files.items():
            if object_name is None:
                object_name = os.path.basename(file_path)

            # Upload the file
            s3_client = boto3.client('s3', aws_access_key_id=aws_key,
                                     aws_secret_access_key=aws_secret)
            try:
                response = s3_client.upload_file(file_path, bucket, location+object_name)
                print("Info: Done uploading " + str(file_path))
            except ClientError as e:
                logging.error(e)

    @staticmethod
    def save_local(df, name):
        to_upload = "data/" + name
        S3Loader.upload_files[to_upload] = name
        try:
            df.to_csv(to_upload, index=False)
            print("Info: Successfully saved " + to_upload)
        except Exception as e:
            print("Error: ", e)

    @staticmethod
    def save_local_model(model, name):
        # name = type(model.estimator).__name__+ "__"+ str(datetime.datetime.today().date())+ ".pkl"
        to_upload = name[0]
        S3Loader.upload_files[to_upload] = name[0].split("/")[1]
        try:
            file = open(to_upload, 'wb')
            pickle.dump(model, file)
            print("Info: Successfully saved " + to_upload)
        except Exception as e:
            print("Error: ", e)


