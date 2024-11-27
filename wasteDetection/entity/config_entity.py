import os
import sys

from dataclasses import dataclass
from wasteDetection.constant.training_pipeline import *
from datetime import datetime


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