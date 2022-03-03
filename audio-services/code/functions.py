import shutil
import logging
import os
import uuid
from AppLoger import AppLoger

def zip_folder(in_path : str, output_filename : str):
    app_guid = os.environ.get('app_guid', 'temp-log')
    logger = AppLoger.getLogger(app_guid)
    logger.debug('zipping folder: {0} with name {1}'.format(in_path, output_filename) )
    return shutil.make_archive(output_filename, 'zip', in_path)

def delete_non_empty_folder(path_to_dir):
    app_guid = os.environ.get('app_guid', 'temp-log')
    logger = AppLoger.getLogger(app_guid)
    
    logger.debug('removing folder {} and all its contents'.format(path_to_dir) )
    shutil.rmtree(path_to_dir)
