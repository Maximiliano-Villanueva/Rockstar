import logging
import os
import sys
from glob import glob
from Abstrac_Handler import AbstractHandler

sys.path.append(os.getenv.get('root_dir'))

from AppLoger import AppLoger



@AbstractHandler.register
class FileHandler(AbstractHandler):
    """
    This class implements the handling of assets in file/dir format
    """
    def __init__(self):
        AbstractHandler.__init__(self)

    def write(self, **kargs):
        """
        implemententation of base class
        request -> flask file upload object
        path -> output path
        """
        logging = self.logging
        #validate params
        requested_params = ['request', 'path', 'filename']

        if not self.validateParameter(parameter = requested_params, param_list = kargs):
            logging.error('error calling function {0}, missing parameters'.format('write'))
            raise Exception('parameters {0} are required'.format(str(requested_params)))

        
        audio = kargs['request']
        path = kargs['path']

        uploads_dir = os.getenv.get('UPLOADS_DIR')
        root_dir = os.getenv.get('root_dir')
        abs_path = os.path.join(root_dir,uploads_dir)

        try:
            audio.save(abs_path)
        except Exception as error:
            logging.error('error saving file {}: '.format(audio.filename))
            raise Exception(error)

        
    
    
    def read(self, **kargs):
        """
        implemententation of base class
        """
        logging = self.logging
        
        requested_params = ['path']
        if not self.validateParameter(parameter = requested_params, param_list = kargs):
            logging.error('error calling function {0}, missing parameters'.format('read'))
            raise Exception('parameters {0} are required'.format(str(requested_params)))

        #get parameters
        path = kargs['path']
        filter = kargs['filter'] if 'filter' in kargs.keys() else '*'
        
        #fetch data
        results = glob(os.path.join(path, filter))
        results =[os.path.basename(r) for r in results]
        return results

        pass
