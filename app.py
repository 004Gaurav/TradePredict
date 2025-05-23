import sys
import os
sys.path.append(os.path.join(os.getcwd(), "src"))


from Trade_prediction_system.logger import logging
from Trade_prediction_system.exception import CustomException
import sys
from Trade_prediction_system.components.data_ingestion import DataIngestion, DataIngestionConfig

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        #python data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)