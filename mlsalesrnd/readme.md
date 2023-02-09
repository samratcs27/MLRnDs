How to set up run script at Jenkins:
Inside execute Shell, type the following:

cat requirements.txt
pip install -r requirements.txt
cd mlsalesrnd/
python main/trainUtil/main.py


In resource/config.json
"bucket_name_dumps": give a bucket name
"aws_key": give ur key,
"aws_secret": give secret key

Inside ur S3 bucket, create a directory called "samplernd".
Inside this folder, upload the following files: car_data.csv, predict_data.csv
