import logging

''' Logging '''
logging.basicConfig(format='%(asctime)s [%(levelname)-8s] %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def write_log(log_type, msg):
    if log_type == 'INFO':
        logger.info(msg)
    elif log_type == 'ERROR':
        logger.error(msg)
    elif log_type == 'DEBUG':
        logger.debug(msg)
