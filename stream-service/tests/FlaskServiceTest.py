import sys, os
import unittest
import requests as req
import json
CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..','code')
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
        

    def test_song_retrieval(self):
        """
        test request for chords
        """
        result = req.get(
            url = 'http://localhost:8081/songs'
        )

        song_list = json.loads(result.content)
        self.assertGreater(len(song_list),0)
    
    
if __name__ == '__main__':
    unittest.main()