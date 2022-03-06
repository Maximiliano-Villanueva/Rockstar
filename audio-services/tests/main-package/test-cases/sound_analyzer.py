import sys
import os
import uuid
import unittest

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..','code')
sys.path.append(CODE_DIR)

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..','code', 'sound-analyze')
sys.path.append(CODE_DIR)

from AppLoger import AppLoger


class FunctionsBlackBox(unittest.TestCase):

    """
    Blackbox testing for the functions file
    """

    def setUp(self):
        """
        create the logger
        """
        self._createLogger()
        from analyzer import ChordExtractor

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

    def test_checkCoords(self):

        #create temp dir and file
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        file_name = 'other.wav'

        #create temp dir and file
        input_dir_path = os.path.join(ROOT_DIR, '..', '..','mock_input')
        input_file_path = os.path.join(input_dir_path, file_name)

        extractor = ChordExtractor()
        chords = extractor.extractChords(input_file_path)

        self.assertGreater(len(chords), 0)


if __name__ == '__main__':
    unittest.main()