

from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import os,sys

class DataValidation:
    
    def __init__(self, data_validation_config:DataValidationConfig,
    data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e :
            raise HousingException(e,sys) from e 
    
    def does_train_test_file_exist(self) -> bool:
        try:
            logging.info("Checking if train and test files are available")
            does_train_file_exist = False
            does_train_file_exist = False
            
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            does_train_file_exist = os.path.exists(train_file_path)
            does_test_file_exist = os.path.exists(test_file_path)
            
            are_available = does_train_file_exist and does_test_file_exist
            
            logging.info(f"Train and test files are available: {are_available}")
            
            if not are_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path
                
                message = f"Training file: {training_file} or Testing file: {testing_file} are not available"
                raise Exception(message)
            
            return are_available
                    
        except Exception as e :
            raise HousingException(e,sys) from e
    
    def validate_dataset_schema(self) -> bool:
        try:
            validation_status = False
            # assignment : validate training and testing dataset using schema file
            #1. number of columns 
            #2. check the value of ocean proximity
            # acceptable values of ocean proximity are: <1H OCEAN, INLAND, NEAR OCEAN, NEAR BAY, ISLAND
            #3. check column names
            
            
            validation_status = True
            return validation_status
        except Exception as e :
            raise HousingException(e,sys) from e
        
    
    def initiate_data_validation(self):
        try:
            self.does_train_test_file_exist()
            self.validate_dataset_schema()
            
            
        except Exception as e :
            raise HousingException(e,sys) from e
        