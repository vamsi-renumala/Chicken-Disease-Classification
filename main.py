from CnnClassifier import logger
from CnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CnnClassifier.pipeline.stage_03_prepare_callbacks import PrepareCallbacksTrainingPipeline
from CnnClassifier.pipeline.stage_04_training import ModelTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>> {STAGE_NAME} started <<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>> {STAGE_NAME} completd <<<<')
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME = 'Prepare Base Model Stage'

try:
    logger.info(f'>>>> {STAGE_NAME} started <<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>> {STAGE_NAME} completed')
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME = 'PREPARE CALLBACKS STAGE'
try:
    logger.info(f'>>>> {STAGE_NAME} started <<<<')
    obj = PrepareCallbacksTrainingPipeline()
    obj.main()
    logger.info(f'>>>> {STAGE_NAME} ended <<<<')
except Exception as e:
    logger.exception(e)
    raise e





STAGE_NAME = 'MODEL TRAINING STAGE'
try:
    logger.info(f'>>>> {STAGE_NAME} started <<<<')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>> {STAGE_NAME} ended <<<<')
except Exception as e:
    logger.exception(e)
    raise e