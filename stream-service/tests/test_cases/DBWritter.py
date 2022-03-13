import unittest
import sys, os
from pathlib import Path
import uuid
from dotenv import load_dotenv


curr_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = Path(os.path.join(curr_dir, '..')).resolve()
sys.path.append(os.path.join(root_dir, 'mock_input'))
from MockAudio import Audio


CODE_DIR = Path(os.path.join(root_dir, '..', 'code')).resolve()

load_dotenv(os.path.join(CODE_DIR,'.env'))
#HANDLERS_DIR = Path(os.path.join(root_dir, '..', 'code', 'asset_handlers')).resolve()
HANDLERS_DIR = os.path.join(root_dir, '..', 'code', 'asset_handlers')
sys.path.append(CODE_DIR)
sys.path.append(HANDLERS_DIR)


from db_writer import MysqlConnector
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

    def readBinaryContent(self, path):
        """
        read file data as binary content
        """
        
        with open(path, 'rb') as audio_file:
            bin_content = audio_file.read()

        return bin_content

    def test_write_to_db(self):
        """
        test exception with invalid parameter
        """
        # mysql -u user -p audio_service
        # mariadb -u user -p audio_service
        #get the list of files
        db_conn = MysqlConnector(host = os.getenv("MYSQL_HOST"), user = os.getenv("MYSQL_USER"), password = os.getenv("MYSQL_PASSWORD"), database = os.getenv("MYSQL_DB"))

        #https://pynative.com/python-mysql-blob-insert-retrieve-file-image-as-a-blob-in-mysql/

        #load file for testing
        curr_dir = os.path.dirname(os.path.abspath(__file__))
        file_dir = Path(os.path.join(curr_dir, '..', 'test_input', 'come.mp3')).resolve()

        #read file
        bin_content = self.readBinaryContent(file_dir)



        db_conn.write(query = "INSERT INTO audio ( title, content) values (%s,%s)", values = [('come.mp3', bin_content)])

        self.assertRaises(1, 1)
        

unittest.main()

        

