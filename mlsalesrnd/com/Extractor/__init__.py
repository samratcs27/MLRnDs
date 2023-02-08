
import pickle
import boto3
import pandas as pd
from com.MLUtils import RFModelTrainer


class S3Extractor:
    def __init__(self, aws_key, aws_secret):
        self.aws_key = aws_key
        self.aws_secret = aws_secret

    def download_file(self, bucket_name, location, save_as=None):
        for file in range(len(location)):
            s3_client = boto3.client('s3', aws_access_key_id=self.aws_key,
                                     aws_secret_access_key=self.aws_secret)
            print("Info: Starting downloading " + location[file])
            try:
                s3_client.download_file(bucket_name, location[file], save_as[file])
                print("Info filed saved here",save_as[file])
                df_file = pd.read_csv(save_as[file])
                print("Info: Downloaded file, saved as ", save_as[file])
                flag = True
            except Exception as e:
                print("Error: ", e)
                df_file = None
                flag = False
            if flag:
                return df_file
            else:
                print("Error: File not saved ", file)



    def download_model(self, bucket_name, location, save_as=None):

        for file in range(len(location)):
            s3_client = boto3.client('s3', aws_access_key_id=self.aws_key,
                                     aws_secret_access_key=self.aws_secret)
            print("Info: Starting downloading " + location[file])

            try:
                s3_client.download_file(bucket_name, location[file], save_as[file])
                print("Info filed saved here",save_as[file])
                filename = open(save_as[file], 'rb')
                model = pickle.load(filename)
                print("Info: Downloaded file, saved as ", save_as[file])
                RFModelTrainer.model = model
                return True
            except Exception as e:
                print("Error: ", e)
                return False


