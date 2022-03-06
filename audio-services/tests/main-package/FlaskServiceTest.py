import sys, os
import unittest
import requests as req

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..','code')
sys.path.append(CODE_DIR)

from AppLoger import AppLoger

class FlaskService(unittest.TestCase):

    """
    Blackbox testing for the functions file
    """

    def setUp(self):
        """
        create the logger
        """
        pass

    def test_upload_file(self):
        """
        test request for chords
        """
        
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(ROOT_DIR, '..', 'mock_input', 'audio_example.mp3')
        files = {'audio': open(file,'rb')} 
        result = req.post(
            url = 'http://localhost:8081/upload'
            , files = files
        )

        files['audio'].close()
        print(result)

    
    def test_extract_chords(self):
        
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(ROOT_DIR, '..', 'mock_input', 'audio_example.mp3')
        files = {'audio': open(file,'rb')} 
        result = req.post(
            url = 'http://localhost:8081/extract_chords?stem=other'
            , files = files
        )

        files['audio'].close()
        
        print(result)

    
if __name__ == '__main__':
    unittest.main()