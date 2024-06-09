from cnnclassifier import logger 
from cnnclassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnclassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
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
