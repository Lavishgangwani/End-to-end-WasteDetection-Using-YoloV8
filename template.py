import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]:%(message)s:")


project_name= "wasteDetection"

lists_of_files = [
    ".github/workflow/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    "data/.gitkeep",
    "research/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",

]


for files in lists_of_files:
    filepath = Path(files)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File: {filepath} already exists")
