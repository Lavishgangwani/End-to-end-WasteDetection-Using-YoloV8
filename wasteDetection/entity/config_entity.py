import os
from dataclasses import dataclass
from wasteDetection.constant.training_pipeline import *



@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR



training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig() 


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )

    data_download_api: str = DATA_DOWNLOAD_API



@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR_NAME
    )

    valid_status_file_dir: str = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)

    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILES
