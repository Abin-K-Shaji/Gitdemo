import logging
def test_log():
    logger=logging.getLogger(__name__)
    filelog=logging.FileHandler("loger.log")
    formatter=logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    filelog.setFormatter(formatter)
    logger.addHandler(filelog)
    logger.setLevel(logging.INFO)

    logger.debug("Error occurred")
    logger.info("info statement")
    logger.warning("something is wrong")
    logger.error("major error occurred")
    logger.critical("critical issues located")
