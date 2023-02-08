
import os
import sys

import warnings
sys.path.insert(0, os.getcwd())
from com.MLUtils import RFModelTrainer
# sys.path.insert(0, '/var/lib/jenkins/jobs/seasonal/workspace')

from com.Loader import S3Loader
from com.Extractor import S3Extractor
from globalClass import All
from utils import generic_config

warnings.filterwarnings('ignore')

if __name__ == "__main__":
    os.makedirs('data', exist_ok=True)
    print(os.getcwd())
    print("*****Info: Started Main*****")
    All.original_dir = os.path.dirname(os.path.realpath(__file__))
    All.config = generic_config(os.getcwd())

    extractor = S3Extractor(aws_key=All.config["aws_key"], aws_secret=All.config["aws_secret"])
    data = extractor.download_file(bucket_name=All.config['bucket_name_dumps'],
                                   location=All.config['path_to_download'],
                                   save_as=All.config['path_to_save'])

    if data is not None:
        model= RFModelTrainer.trainData(data);
        print(str(model));
        S3Loader.save_local_model(model, All.config['path_to_save_model'])
        S3Loader.upload_file_to_S3(bucket=All.config['bucket_name_dumps'], aws_key=All.config["aws_key"],
                                   aws_secret=All.config["aws_secret"],
                                   location=All.config['path_to_upload'])


    else:
        print("No data for training Found!!")





