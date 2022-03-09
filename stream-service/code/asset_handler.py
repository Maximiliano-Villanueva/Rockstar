
class AssetHandler:
    """
    this singletone class handles the access to assets
    """
    handler = None
    logger = None
    
    @staticmethod
    def setHandler(new_handler):
        """
        set a new handler
        """
        handler = new_handler

    @staticmethod
    def write(sentence, values = None):
        """
        call the write function of the handler
        """
        if logger is not None:
            logger.info('entering write method of AssetHandler')
        return handler.write(sentence, values)

    @staticmethod
    def read(sentence):
        """
        call the read function of the handler
        """
        if logger is not None:
            logger.info('entering read method of AssetHandler')
        return handler.get(sentence)

    @staticmethod
    def update(sentence):
        """
        call the read function of the handler
        """
        if logger is not None:
            logger.info('entering update method of AssetHandler')
            
        return handler.update(sentence)

    