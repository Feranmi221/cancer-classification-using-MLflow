# import zipfile

# def is_zipfile(filepath):
#     return zipfile.is_zipfile(filepath)

# print(is_zipfile('artifacts\data_ingestion\data.zip'))

# def check_file_header(filepath):
#     with open(filepath, 'rb') as f:
#         header = f.read(4)
#         return header

# header = check_file_header('artifacts\data_ingestion\data.zip')
# print(f"File header: {header}")
import os
import zipfile
# print(os.getcwd())
# print(os.path.isfile('artifacts\data_ingestion\data.zip'))

import os
import zipfile
import gdown
from cnnclassifier import logger
from cnnclassifier.utils.common import get_size
from cnnclassifier.entity.config_entity import DataIngestionConfig
from 
class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    
    def download_file(self) ->str:
        '''
        Fetch data from the url
        '''
        try: 
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion",exist_ok = True)
            if os.path.isfile('artifacts\data_ingestion\data.zip') == False:
                logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
                file_id = dataset_url.split("/")[-2]
                prefix = 'https://drive.google.com/uc?/export=download&id='
                gdown.download(prefix + file_id,zip_download_dir)
                logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
    
data_ingest = DataIngestion()
data_ingest.extract_zip_file()
