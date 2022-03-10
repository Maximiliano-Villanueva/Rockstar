
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
    def write(**kargs):
        """
        call the write function of the handler
        """
        
        if AssetHandler.logger is not None:
            AssetHandler.logger.info('entering write method of AssetHandler')
        
        return AssetHandler.handler.write(**kargs)

    @staticmethod
    def read(**kargs):
        """
        call the read function of the handler
        """
        
        if AssetHandler.logger is not None:
            AssetHandler.logger.info('entering read method of AssetHandler')
        
        return AssetHandler.handler.read(**kargs)

    @staticmethod
    def update(sentence):
        """
        call the read function of the handler
        """
        
        if AssetHandler.logger is not None:
            AssetHandler.logger.info('entering update method of AssetHandler')
        
        return AssetHandler.handler.update(sentence)

    