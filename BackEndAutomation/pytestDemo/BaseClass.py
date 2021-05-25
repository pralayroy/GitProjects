import inspect
import logging


class BaseClass:
    def getLogger(self):
        testCaseName = inspect.stack()[1][3]
        logger = logging.getLogger(testCaseName)
        fileHandler = logging.FileHandler("logfile.log")
        logger.addHandler(fileHandler)
        forMatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        fileHandler.setFormatter(forMatter)
        logger.setLevel(logging.INFO)
        return logger
