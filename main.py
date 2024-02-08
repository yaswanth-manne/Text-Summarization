from TextSummarization.pipeline.stage_01 import DataIngestionTrainPipeline
from TextSummarization.logging import logger

STAGE_NAME = "Data Ingestion Satge"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\n x====================================x")
except Exception as e:
    logger.exceptiion(e)
    raise e
