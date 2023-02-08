import os

from setuptools import find_packages
from setuptools import setup
# botocore-1.18.18
requires = (
    "boto3==1.19.8",
    "botocore==1.22.8",
    "numpy==1.21.2",
    "pandas==1.0.5",
    "scikit_learn==1.2.1"
)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="mlsalesrnd",
    version="0.0.1",
    author="mudassar",
    author_email="NA",
    description="machine learning mlsalesrnd lib and utils",
    packages=find_packages(include=['mlsalesrnd', 'mlsalesrnd*']),
    url="url",
    install_requires=requires,
    python_requires='>=3.6'
)
