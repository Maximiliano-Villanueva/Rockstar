import unittest
import sys, os
from pathlib import Path
import uuid

curr_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = Path(os.path.join(curr_dir, '..')).resolve()
sys.path.append(os.path.join(root_dir, 'mock_input'))
from MockAudio import Audio


CODE_DIR = Path(os.path.join(root_dir, '..', 'code')).resolve()
#HANDLERS_DIR = Path(os.path.join(root_dir, '..', 'code', 'asset_handlers')).resolve()
HANDLERS_DIR = os.path.join(root_dir, '..', 'code', 'asset_handlers')
sys.path.append(CODE_DIR)
sys.path.append(HANDLERS_DIR)


from file_writer import FileHandler
from AppLoger import AppLoger


class FileWriterTest(unittest.TestCase):

    CURR_DIR = os.path.dirname(os.path.abspath(__file__))
    """
    Blackbox testing for the FilleWriter class
    """

    def setUp(self):
        """
        create the logger
        """
        self._createLogger()

    def _createLogger(self):
        """
        create logger
        """
        #create guid
        uuid_session = uuid.uuid4()
        uuid_session_str = str(uuid_session)
        os.environ['app_guid'] = str(uuid_session)

        #creat apploger
        AppLoger.create_logger(guid = uuid_session_str, log_name=str(type(self)))
        self.logger = AppLoger.getLogger(uuid_session_str)

    def test_create_file(self):
        """
        test creation of file
        """
        #assign env variables since these are requested in the write method of the filehandler
        os.environ['UPLOADS_DIR'] = 'tmp_files'
        os.environ['root_dir'] = str(Path(os.path.join(FileWriterTest.CURR_DIR, '..')).resolve())

        #create path for test file
        input_file = Path(os.path.join(os.environ['root_dir'], 'test_input', 'file_example.txt')).resolve()

        #create mock object for audio
        tmp_audio = Audio('filename.txt')
        
        #write file to path
        fh = FileHandler()
        fh.write(path = input_file, request = tmp_audio)

        self.assertTrue(os.path.exists(input_file))

        os.remove(input_file)

    def test_create_file_invalid_folder1(self):
        """
        test creation of file
        """
        #assign env variables since these are requested in the write method of the filehandler
        os.environ['UPLOADS_DIR'] = 'tmp_files'
        os.environ['root_dir'] = str(Path(os.path.join(FileWriterTest.CURR_DIR, '..')).resolve())

        #create path for test file
        input_file = Path(os.path.join(os.environ['root_dir'], 'test_input2', 'file_example.txt')).resolve()

        #create mock object for audio
        tmp_audio = Audio('filename.txt')
        
        #write file to path
        fh = FileHandler()
        

        self.assertRaises(Exception, lambda : fh.write(path = input_file, request = tmp_audio))

    def test_read_file(self):

        #create path to store the file
        root_dir = str(Path(os.path.join(FileWriterTest.CURR_DIR, '..')).resolve())
        input_file = Path(os.path.join(root_dir, 'test_input')).resolve()

        #create temp file
        random_name = str(uuid.uuid4())
        with open(os.path.join(input_file, random_name), 'w') as random_file:
            random_file.write('test')
        
        #get the list of files
        fh = FileHandler()
        file_list = fh.read(path=input_file)
        
        #remove temp file
        os.remove(os.path.join(input_file, random_name))

        self.assertTrue(random_name in file_list)
        

    def test_read_file_no_path_param(self):
        """
        test exception with invalid parameter
        """
        #get the list of files
        fh = FileHandler()
        
        self.assertRaises(Exception, lambda : fh.read())

    def test_read_file_invalid_path_param(self):
        """
        test exception with invalid parameter
        """
        #get the list of files
        fh = FileHandler()
        
        self.assertRaises(Exception, lambda : fh.read('test'))
        

unittest.main()

        

