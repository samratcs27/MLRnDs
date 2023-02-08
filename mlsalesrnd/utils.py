__author__ = 'kanishk@applicate'

import json
import os
from datetime import datetime

from globalClass import All


def readFilePath(path):
    f = open(path)
    data = json.load(f)
    f.close()
    return data


def read_config_file():
    config_file_name = "config.json"
    config_file = "resource/" + config_file_name
    config = readFilePath(config_file)
    print("Info: Using " + str(config))
    return config


def change_dir_to_mlsalesrnd():
    print("Info: Original dir", All.original_dir)
    dir = All.original_dir.split("mlsalesrnd")[0] + "/mlsalesrnd"
    os.chdir(dir)
    print("Info: Changed dir", os.getcwd())


def change_dir_to_original():
    print("Info: Current dir ", os.getcwd())
    os.chdir(All.original_dir)
    print("Info: Changed dir", os.getcwd())


def generic_config(path):
    conf = read_config_file()
    return conf


def get_first_date_of_current_month():
    today = datetime.today().date()
    first_date_of_current_period = datetime(today.year, today.month, 1).date()
    if today != first_date_of_current_period:
        return 0
    else:
        return 1


def filter_sales_data(df):
    df = df.drop_duplicates()
    df = df[['piece_quantity', 'skucode', 'net_amount', 'outletcode', 'creation_time']]
    df = df[((df['net_amount'] > 0) & (df['piece_quantity'] >= 1))]
    df = df.reset_index(drop=True)
    print("Info: len of sales data after filter",len(df))
    return df


if __name__ == "__main__":
    from com.Extractor import S3

    extractor_obj = S3('test_key', 'test_sec')
    config = generic_lob_file(os.getenv("LOB"), 'test_down', 'test_up')
    print(config)
