import logging
import time
import os

save_dir = time.strftime('./%Y-%m-%d-%H-%M-%S', time.localtime())
os.mkdir(save_dir)

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
log_save_dir = os.path.join(save_dir, 'log.txt')
handler = logging.FileHandler(log_save_dir)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
 
logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
