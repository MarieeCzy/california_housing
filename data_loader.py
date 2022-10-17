import os
from urllib import request

#download housing.csv file from git repository, make new directory datasets/housing/ and save housing.csv 
DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join('datasets', 'housing')
HOUSING_URL = DOWNLOAD_ROOT + 'datasets/housing/housing.csv'

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    os.makedirs(housing_path, exist_ok=True)
    local_path = os.path.join(housing_path, 'housing.csv')
    request.urlretrieve(housing_url, local_path)

    
fetch_housing_data()

