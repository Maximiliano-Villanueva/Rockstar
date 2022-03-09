import abc
import os, sys
from pathlib import Path
curr_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.join(curr_dir, '..')

sys.path.append(root_dir)
from AppLoger import AppLoger

class AbstractHandler(metaclass=abc.ABCMeta):

    def __init__(self):
        #get app loger
        app_guid = os.environ.get('app_guid', 'temp-log')
        self.logging = AppLoger.getLogger(app_guid)

    
    @abc.abstractmethod
    def write(self, **kargs):
        pass

    @abc.abstractmethod
    def read(self, **kargs):
        pass
    
    def validateParameter(self,parameter, param_list):
        """
        validate parameters
        parameter -> str or list<str>: name of parameters to check
        param_list -> list or dict of parameters
        """
        param_list = set(param_list if isinstance(param_list, list) else param_list.keys())
        parameter = set(parameter if isinstance(parameter, list) else [parameter])

        return parameter.issubset(param_list)
