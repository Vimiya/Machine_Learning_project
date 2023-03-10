import logging
from datetime import datetime

import os
# we are going to store all logging file in LOG_DIR
LOG_DIR="housing_logs"

CURRENT_TIME_STAMP=f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}" #gives us current timestamp

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"

# check directory exists or not, if not then create directory (import os)
os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s %(message)s',
level=logging.INFO
)

 