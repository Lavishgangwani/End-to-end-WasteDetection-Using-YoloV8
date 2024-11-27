import os
import yaml
from ensure import ensure_annotations
import base64

from wasteDetection import logger
from box import ConfigBox
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(file_path: str) -> dict:
    """
    Reads a YAML file and returns a dict object
    :param file_path: path of the YAML file
    :return: dict object
    """
    try:
        with open(file_path, 'rb') as file:
            yaml_data = yaml.safe_load(file)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(yaml_data)
    except BoxValueError as e:
        raise Exception(f"error occurred while reading YAML file: {file_path}")
    except Exception as e:
        raise e
    



@ensure_annotations
def write_yaml(file_path: str, content:object, replace:bool=False) -> None:
    try:

        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, 'w') as file:
            yaml.dump(content, file)
            logger.info(f"yaml file: {file_path} has been saved")

    except Exception as e:
        raise e
    

@ensure_annotations
def decodeImage(imageString, filename):
    with open("./data/" + filename, 'wb') as f:
        f.write(imageString)
        f.close()



@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
    

