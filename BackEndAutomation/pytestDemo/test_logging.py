import inspect
import logging


def test_logging():
    testCaseName = inspect.stack()[1][3]
    logger = logging.getLogger(testCaseName)
    fileHandler = logging.FileHandler("logfile.log")
    logger.addHandler(fileHandler)
    forMatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
    fileHandler.setFormatter(forMatter)
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement executed")
    logger.info("A info statement")
    logger.error("An error occured")
    logger.warning("Something is in warning mode")
    logger.critical("Critical issue")
