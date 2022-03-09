import logging
import os
import sys
from glob import glob
from Abstrac_Handler import AbstractHandler

curr_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(curr_dir, '..')
sys.path.append(root_dir)

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
        path -> input path

        dependencies :
            - environment : UPLOADS_DIR, root_dir
        requires : 
        returns bool : Tells if operation was successful
        """

        logging = self.logging
        #validate params
        requested_params = ['request']

        if not self.validateParameter(parameter = requested_params, param_list = kargs):
            logging.error('error calling function {0}, missing parameters'.format('write'))
            raise Exception('parameters {0} are required'.format(str(requested_params)))

        
        audio = kargs['request']

        #get paths
        uploads_dir = os.environ.get('UPLOADS_DIR')
        root_dir = os.environ.get('root_dir')
        abs_path = os.path.join(root_dir,uploads_dir)

        abs_path = abs_path if 'path' not in kargs.keys() else kargs['path']
        
        if not os.path.exists(os.path.dirname(abs_path)):
            raise Exception('path {0] does not exist'.format(abs_path))
        try:
            audio.save(abs_path)
        except Exception as error:
            logging.error('error saving file {}: '.format(audio.filename))
            raise Exception(error)

        return True
        
    
    
    def read(self, **kargs):
        """
        implemententation of base class
        path -> str : path where to read files from
        [filter] -> str -> filter for glob. default : '*'

        returns list of strings
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
