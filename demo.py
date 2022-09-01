from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation
import os 

def main(): 
    try:
        
        config_path = os.path.join('config', 'config.yaml')
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed")
        # data_validation_config = Configuration().get_data_validation_config()
        # print(data_validation_config)
        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)
        # schema_file_path = r"C:\Users\Amit\Documents\projects\ml project\ML_project\config\schema.yaml"
        # file_path = r"C:\Users\Amit\Documents\projects\ml project\ML_project\housing\artifact\data_ingestion\2022-08-23-18-22-28\ingested_data\train\housing.csv"
        # df = DataTranformation.validate_dtypes_of_dataframe_and_schema_columns(file_path=file_path, schema_file_path=schema_file_path)
        # print(df.columns)
        # print(df.dtypes)
        
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)
    
if __name__=="__main__":
    main()