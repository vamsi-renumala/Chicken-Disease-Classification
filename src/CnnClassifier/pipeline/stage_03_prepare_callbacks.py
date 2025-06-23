from CnnClassifier.components.prepare_callbacks import PrepareCallbacks
from CnnClassifier.config.congfiguration import ConfigurationManager
from CnnClassifier import logger

STAGE_NAME = 'PREPARE CALLBACKS STAGE'

class PrepareCallbacksTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config= prepare_callbacks_config)
        callbacks_list = prepare_callbacks.get_tb_ckpt_callbacks()


    
if __name__ == '__main__':
    try:
        logger.info(f'>>>> {STAGE_NAME} started <<<<')
        obj = PrepareCallbacksTrainingPipeline()
        obj.main()
        logger.info(f'>>>> {STAGE_NAME} ended <<<<')
    except Exception as e:
        logger.exception(e)
        raise e