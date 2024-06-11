from cnnclassifier import logger 
from cnnclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnclassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnclassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnclassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e :
    logger.exception(e)
    raise e

STAGE_NAME = "prepare base model"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj2 = PrepareBaseModelTrainingPipeline()
        obj2.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x")
except Exception as e :
        logger.exception(e)
        raise e

STAGE_NAME = "Training"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj3 = ModelTrainingPipeline()
    obj3.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj4 = EvaluationPipeline()
    obj4.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e