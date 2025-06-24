from CnnClassifier.components.prepare_callbacks import PrepareCallbacks
from CnnClassifier.components.training import Training
from CnnClassifier.config.congfiguration import ConfigurationManager
from CnnClassifier import logger

STAGE_NAME = 'MODEL TRAINING STAGE'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


if __name__ == '__main__':
    try:
        logger.info(f'>>>> {STAGE_NAME} started <<<<')
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>> {STAGE_NAME} completed <<<<')
    except Exception as e:
        logger.exception(e)
        raise e




