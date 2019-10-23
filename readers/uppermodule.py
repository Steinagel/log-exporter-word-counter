import logging.config
from readers import lowermodule
import traceback 

logging.config.fileConfig('configs/logging.ini', disable_existing_loggers=False)
logger = logging.getLogger((__name__).split(".")[1])

def record_word_count(myfile):
    try:
        lowermodule.word_count(myfile)
        logger.debug(f"{__name__} finished saving metrics from the file %s", myfile)
    except OSError as e:
        logger.error(e)
