from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter
import os
from AppLoger import AppLoger

app_guid = os.environ.get('app_guid', 'temp-log')
logging = AppLoger.getLogger(app_guid)

class AudioSpleeter:
    """
    this class splits audio using the spleeter library from deezer
    """

    def __init__(self):
        self.separator = Separator('spleeter:5stems')
        self.sample_rate = 44100
    
    def separate(self, audio_input, output_dir = 'output'):
        """
        separate the audio into 5 files (5 stems)
        """
        #convert audio_input to list
        logging.info('entering function separate in class {0}, audio_input = {1}'.format('AudioSpleeter',audio_input))
        audio_list = [audio_input] if not isinstance(audio_input, list) else audio_input
        file_paths = []

        logging.info('processing {0} files'.format(str(len(audio_list))))

        for audio_input in audio_list:
            if not os.path.exists(audio_input):
                raise Exception("file: {0} not found".format(audio_input))
            logging.debug('separating file {0}'.format('audio_input'))

            audio_loader = AudioAdapter.default()
            waveform, _ = audio_loader.load(audio_input, sample_rate=self.sample_rate)

            self.separator.separate_to_file(audio_input, output_dir, synchronous=False)

            #remove extension from filename
            file_name = os.path.basename(audio_input)
            file_name = '.'.join(file_name.split('.')[:-1])
            file_paths.append(os.path.join(output_dir, file_name))
        
        logging.debug('waiting for threads to join')
        self.separator.join()

        logging.info('end function separate in class {0}'.format('AudioSpleeter',audio_input))

        return file_paths