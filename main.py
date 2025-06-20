from CnnClassifier import logger
from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>> {STAGE_NAME} started <<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>> {STAGE_NAME} completd <<<<')
except Exception as e:
    logger.exception(e)
    raise e
