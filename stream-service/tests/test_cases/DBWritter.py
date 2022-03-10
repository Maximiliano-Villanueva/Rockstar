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


from db_writter import MysqlConnector
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

    def test_write_to_db(self):
        """
        test exception with invalid parameter
        """
        #get the list of files
        db_conn = MysqlConnector(host = os.getenv("MYSQL_HOST"), user = os.getenv("MYSQL_USER"), password = os.getenv("MYSQL_PASSWORD"), database = os.getenv("MYSQL_DB"), logger = logger)

        db_conn.write("INSERT INTO song (title) values ('test')")

        self.assertRaises(1, 1)
        

unittest.main()

        

