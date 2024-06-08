from src.StudentsPerformancePrediction.logger import logging
from src.StudentsPerformancePrediction.exception import CustomException
from src.StudentsPerformancePrediction.components.data_ingestion import DataIngestion
from src.StudentsPerformancePrediction.components.data_ingestion import DataIngestionConfig
from src.StudentsPerformancePrediction.components.data_transformation import DataTransformationConfig,DataTransformation
import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        data_ingestion=DataIngestion()
        train_data_path,test_data_path= data_ingestion.initiate_data_ingestion()
        
        data_transformation =DataTransformation()
        data_transformation.initiate_data_transformer(train_data_path,test_data_path)
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)