import logging
import os.path


class LonGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=os.path.join(".\\Logs\\automation.log"),
                            format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %P')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


# class LonGen:
#     @staticmethod
#     def loggen():
#         logger = logging.getLogger()
#         fhandler = logging.FileHandler(filename='mylog.log', mode='a')
#         formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#         fhandler.setFormatter(formatter)
#         logger.addHandler(fhandler)
