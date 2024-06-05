from src.StudentsPerformancePrediction.logger import logging
from src.StudentsPerformancePrediction.exception import CustomException

import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        a=1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise(e,sys)