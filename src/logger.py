import logging
import os
from datetime import datetime as dt

log_file_name = f"{dt.now().strftime('%m-%d-%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs", log_file_name)
os.makedirs(log_path, exist_ok=True)

# log_file_path = os.path.join(log_path, log_file_name)

logging.basicConfig(
    filename = log_file_name,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)
