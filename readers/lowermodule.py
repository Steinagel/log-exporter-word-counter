import logging
from lib.logconfig import filelogger

logger = filelogger((__name__).split(".")[1],[ "filename", "message", "asctime", "name", "levelname", "count" ],'logs/file.log',logging.DEBUG)

def decode_complex(dct):
    sum = 0
    for key in dct:
        sum+=int(key["cont"])
    return()

def word_count(myfile):
    try:
        with open(myfile, 'r') as f:
            file_data = f.read()
            words = file_data.split(" ")
            final_word_count = len(words)
            logger.debug(f"this file has {final_word_count} words", extra={'count':f'{final_word_count}', 'file_processed': f'{myfile}'})
            return final_word_count-1
    except OSError as e:
        logger.error(e)
