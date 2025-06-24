from CnnClassifier.components.evaluation import Evaluation
from CnnClassifier.config.congfiguration import ConfigurationManager
from CnnClassifier import logger

STAGE_NAME = 'MODEL EVALUATION STAGE'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()



if __name__ == '__main__':
    try:
        logger.info(f'>>>> {STAGE_NAME} started <<<<')
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f'>>>> {STAGE_NAME} completed <<<<')
    except Exception as e:
        logger.exception(e)
        raise e






