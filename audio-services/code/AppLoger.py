import logging
import os

class CustomLogger:
    """
    handle custom logs
    """

    def __init__(self, guid, log_name):
        self.guid = guid
        self.logName = log_name
        
        self.init_logger()

    def init_logger(self):
        """
        create a new logger
        """

        app_name = self.logName
        uuid_session_str = str(self.guid)

        log_path = os.path.join('..','logs', app_name)
        log_file_path = os.path.join('..','logs', app_name, app_name + '_' + uuid_session_str + '.log')
        try:
            os.makedirs(log_path)
        except:
            pass
        
        logger = logging.getLogger(app_name)   # > set up a new name for a new logger

        logger.setLevel(logging.DEBUG)  # here is the missing line

        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        filename = log_file_path
        log_handler = logging.FileHandler(filename)
        log_handler.setLevel(logging.DEBUG)
        log_handler.setFormatter(log_format)

        logger.addHandler(log_handler)

        self.logger = logger

class AppLoger:
    """
    handle different logs for the application
    """
    loggers = dict()

    def __init__(self):
        pass
    
    @staticmethod
    def create_logger(guid, log_name):
        """
        add and keep track of a logger
        """
        AppLoger.loggers[guid] = CustomLogger(guid, log_name)
    
    @staticmethod
    def getLoggerClass(guid):
        return AppLoger.loggers[guid]

    @staticmethod
    def getLogger(guid):
        return AppLoger.loggers[guid].logger

