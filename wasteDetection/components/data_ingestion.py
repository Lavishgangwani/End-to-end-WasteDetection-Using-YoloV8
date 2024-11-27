import os
from roboflow import Roboflow
from wasteDetection import logging
from wasteDetection.entity.config_entity import DataIngestionConfig
from wasteDetection.entity.artifacts_entity import DataIngestionArtifact
import shutil


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
            logging.info(f"DataIngestionConfig initialized with: {self.data_ingestion_config}")
        except Exception as e:
            logging.error(f"Error initializing DataIngestion: {e}")
            raise e

    def download_data(self) -> str:
        """
        Downloads data from Roboflow using the provided API key and saves it in the specified directory.

        Returns:
            str: Path to the directory containing the downloaded dataset.
        """
        try:
            dataset_api = self.data_ingestion_config.data_download_api
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok=True)

            logging.info(f"Downloading dataset to temporary directory: {zip_download_dir}")

            # Connect to Roboflow and fetch dataset
            rf = Roboflow(api_key=dataset_api)
            project = rf.workspace("lavishs-cv-projects").project("waste-detection-a6dzt")
            version = project.version(1)
            dataset = version.download("yolov8")

            logging.info(f"Dataset downloaded successfully to: {dataset.location}")

            # Move the downloaded folder to the configured path
            downloaded_path = dataset.location
            final_dataset_path = os.path.join(zip_download_dir, os.path.basename(downloaded_path))

            # Check if a folder with the same name exists
            if os.path.exists(final_dataset_path):
                shutil.rmtree(final_dataset_path)  # Remove it if it exists

            shutil.move(downloaded_path, final_dataset_path)

            logging.info(f"Dataset moved to: {final_dataset_path}")

            # Return the final path to the dataset
            return final_dataset_path

        except Exception as e:
            logging.error(f"Error occurred during dataset download: {e}")
            raise e

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        Initiates the data ingestion process by downloading the dataset.

        Returns:
            DataIngestionArtifact: Contains the path to the downloaded dataset.
        """
        logging.info("Starting data ingestion process.")
        try:
            # Download the data and get the folder path
            final_dataset_path = self.download_data()

            # Create a DataIngestionArtifact instance
            data_ingestion_artifact = DataIngestionArtifact(
                data_file_path=final_dataset_path,
            )

            logging.info(f"Data ingestion process completed successfully. Artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            logging.error(f"Error in initiate_data_ingestion: {e}")
            raise e


if __name__ == "__main__":
    try:
        # Create a config object and initialize DataIngestion
        config = DataIngestionConfig()
        ingestion = DataIngestion(data_ingestion_config=config)
        ingestion_artifact = ingestion.initiate_data_ingestion()
        print(ingestion_artifact)
    except Exception as e:
        logging.error(f"Main execution failed: {e}")
