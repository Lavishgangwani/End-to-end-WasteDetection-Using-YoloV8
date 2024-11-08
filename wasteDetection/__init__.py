import logging
import os
import sys


format = "[%(asctime)s: %(levelname)s: %(name)s: %(filename)s: %(message)s:]"

logs_dir = 'logs'
logs_filename = os.path.join(logs_dir, 'running_logs.log')

os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=format,
    handlers=[
        logging.FileHandler(logs_filename),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)
logger.info('Logging started')