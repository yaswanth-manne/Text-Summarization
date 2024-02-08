from TextSummarization.pipeline.stage_01 import DataIngestionTrainPipeline
from TextSummarization.pipeline.stage_02 import DataValidationTrainPipeline
from TextSummarization.logging import logger

STAGE_NAME = "Data Ingestion Satge"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n x====================================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Satge"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_validation = DataValidationTrainPipeline()
    data_validation.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n x====================================x")
except Exception as e:
    logger.exception(e)
    raise e