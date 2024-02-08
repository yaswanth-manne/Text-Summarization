from TextSummarization.config.configuration import ConfigurationManager
from TextSummarization.componenets.data_validation import DataValidation
from TextSummarization.logging import logger


class DataValidationTrainPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exist()