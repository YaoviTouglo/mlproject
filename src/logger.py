import logging
import os
from datetime import datetime

LOG_FOLDER = f"{datetime.now().strftime('%m_%d_%Y')}"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", LOG_FOLDER)

# Create folder if not exists
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)


# #==================
# if __name__=="__main__":
#     logging.info("Logging has started.")
