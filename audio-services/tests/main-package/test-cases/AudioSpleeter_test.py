#import coverage
import sys, os
import unittest
import uuid
import shutil

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..','code')
print(CODE_DIR)
sys.path.append(CODE_DIR)

from AppLoger import AppLoger


class AudioSpleeterTest(unittest.TestCase):

    """
    Blackbox testing for the functions file
    """

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


            
    def test_black_box_audioSpleet_no_output(self):
        """
        test audio spleeter with default output folder
        """
        self._createLogger()
        from AudioSpleetc import AudioSpleeter
        
        #create temp dir and file
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        input_dir_path = os.path.join(ROOT_DIR, '..', '..','mock_input')
        input_file_path = os.path.join(input_dir_path, 'audio_example.mp3')
        
        out_path = os.path.join(ROOT_DIR, 'output')
        
        audio_spleeter = AudioSpleeter()

        audio_spleeter.separate(input_file_path)
        self.assertEqual(os.path.exists(out_path), True)

        shutil.rmtree(out_path)
        

    def test_black_box_audioSpleet_defined_output(self):
        """
        test the zipping of a folder
        """
        self._createLogger()
        from AudioSpleetc import AudioSpleeter
        
        #create temp dir and file
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        input_dir_path = os.path.join(ROOT_DIR, '..', '..','mock_input')
        input_file_path = os.path.join(input_dir_path, 'audio_example.mp3')
        
        out_path = os.path.join(ROOT_DIR, 'test-output')
        
        audio_spleeter = AudioSpleeter()

        audio_spleeter.separate(input_file_path)

        self.assertEqual(os.path.exists(out_path), True)

        shutil.rmtree(out_path)

    def test_invalid_input_name(self):
        """
        test invalid value for input name parameter
        """
        self._createLogger()
        from AudioSpleetc import AudioSpleeter

        #create temp dir and file
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        input_dir_path = os.path.join(ROOT_DIR, '..', '..','mock_input_invalid')
        input_file_path = os.path.join(input_dir_path, 'audio_example.mp3')
        
        out_path = os.path.join(ROOT_DIR, 'test-output')
        
        audio_spleeter = AudioSpleeter()

        #an exception is expected since the input does not exist
        try:
            #try to create the files
            audio_spleeter.separate(input_file_path)
            #error if no error is thrown
            self.assertEqual(1, 0)
        except:
            #error has been detected
            self.assertEqual(1, 1)

        #attempt to remove any leaking file
        try:
            shutil.rmtree(out_path)
        except:
            pass



unittest.main()