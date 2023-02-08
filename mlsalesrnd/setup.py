import os

from setuptools import find_packages
from setuptools import setup
# botocore-1.18.18
requires = (
    "boto3",
    "botocore",
    "numpy",
    "pandas",
    "scikit_learn"
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
    python_requires='>=3.7'
)
