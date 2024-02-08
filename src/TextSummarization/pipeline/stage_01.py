from TextSummarization.config.configuration import ConfigurationManager
from TextSummarization.componenets.data_ingestion import DataIngestion
from TextSummarization.logging import logger


class DataIngestionTrainPipeline:
    def __init__(self):
        pass

    def main(self):
            config = ConfigurationManager()
            data_ingestion_configuration = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_configuration)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()