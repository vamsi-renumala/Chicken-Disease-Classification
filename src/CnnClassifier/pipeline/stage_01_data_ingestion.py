from CnnClassifier.components.data_ingestion import DataIngestion
from CnnClassifier.config.congfiguration import ConfigurationManager
from CnnClassifier.entity.config_entity import DataIngestionConfig
from CnnClassifier import logger

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config= data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()

# testable independently, also for debugging
if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<')
    except Exception as e:
        logger.exception(e)
        raise e
