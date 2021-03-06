import os
import sys

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(CODE_DIR)

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'external', 'chord_extractor')
sys.path.append(CODE_DIR)

from chord_extractor.extractors import Chordino
from chord_extractor import clear_conversion_cache, LabelledChordSequence
from AppLoger import AppLoger

class ChordExtractor(Chordino):
    """
    this class parses the chords from a file
    """
    def __init__(self):
        """
        basic constructor
        """
        Chordino.__init__(self)
        app_guid = os.environ.get('app_guid', 'temp-log')
        self.logger = AppLoger.getLogger(app_guid)

    
    def extractChords(self, files_path):
        """
        extract the cords from a file or a list of files
        files_path -> str or list
        """
        self.logger.info('start extracting chords in class {0}'.format('ChordExtractor') )
        if files_path is None or (not isinstance(files_path, str) and not isinstance(files_path, list)):
            raise Exception("files_path parameter is neither a list or a string")
        
        files_path = files_path if isinstance(files_path, list) else [files_path]
        # Optionally clear cache of file conversions (e.g. wav files that have been converted from midi)
        clear_conversion_cache()

        # Run bulk extraction
        try:
            res = self.extract_many(files_path, callback=None, max_files_in_cache=10, stop_on_error=False)
        except Exception as error:
            #error parsing files
            self.logger.error('an error ocurred while extracting chords in function extract_many. File list: {0} '.format(str(files_path)))
            self.logger.error(str(error))

            return []

        return res


"""#create temp dir and file
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = 'other.wav'
sound_path = os.path.join(ROOT_DIR, '..', 'output', 'come', file_name)

#visualize(sound_path)

extractor = ChordExtractor()
chords = extractor.extractChords(sound_path)

print(chords)"""

