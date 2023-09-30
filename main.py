from textSummarizer.pipeline.Step1_data_ingestion import DataIngestionTrainingPipeline

from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> Step 1 : {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Step 1 : {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
