
import os
import sys
sys.path.insert(0, os.getcwd())
from com.MLUtils import RFModelTrainer
import warnings
# sys.path.insert(0, '/var/lib/jenkins/jobs/seasonal/workspace')

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
                                   location=All.config['path_to_download_forecast_data'],
                                   save_as=All.config['path_to_save_forecast_data'])

    if data is not None:
        stauts_model_load = extractor.download_model(bucket_name=All.config['bucket_name_dumps'], location=All.config['path_to_download_model'],
                                 save_as=All.config['path_to_save_model']);
        if stauts_model_load:
            print(RFModelTrainer.predictData(data))
    else:
        print("No data for forecast Found!!")





