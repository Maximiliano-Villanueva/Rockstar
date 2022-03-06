from flask import  Flask, render_template, abort, request, send_file, jsonify
from app import app
from main import uploads_dir
import os
import sys
from AudioSpleetc import AudioSpleeter
from functions import *

from AppLoger import AppLoger

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'sound-analyze')
sys.path.append(CODE_DIR)

from analyzer import ChordExtractor



#get app loger
app_guid = os.environ.get('app_guid', 'temp-log')
logging = AppLoger.getLogger(app_guid)

#simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    logging.info('routing to: {0}'.format('index'))
    return render_template('index.html')


@app.route('/test', methods=['GET', 'POST'])
def test():
    logging.info('routing to: {0}'.format('test'))
    return render_template('test.html')


@app.route('/upload', methods=['POST', 'PUT'])
def upload():
    logging.info('routing to: {0}'.format('upload'))
    out_filename = handle_upload(zip_output = True)

    return send_file(out_filename, as_attachment=True)

@app.route('/extract_chords', methods=['POST', 'PUT'])
def extract_chords():
    """
    extract chords from uploaded file
    returns json
    """   
    logging.info('routing to: {0}'.format('extract_chords'))
    logging.debug('entering function: {0}'.format('extract_chords'))

    out_dirname = handle_upload(zip_output = False)

    if out_dirname is None:
        abort(404)
    #get file name
    file = request.args.get('stem', default = 'other')
    logging.debug('stem requested: {0}'.format(file))
    file = file + '.wav'
    file_path = os.path.join(out_dirname, file)
    

    #extract
    extractor = ChordExtractor()
    chords = extractor.extractChords(file_path)

    if len(chords) < 1:
        logging.warn('no chords found in file: {0}'.format(file_path))
        return jsonify({'error', 'no chords found'})

    return jsonify(chords)

    


    


def handle_upload(zip_output = True):
    """
    handle upload of files
    zip_output -> bool : zip the result of separation
    returns -> str : with path to zip file or to folder containing data
    """
    
    logging.info('entering function: {0}'.format('handle_upload'))

    #check if file is attached
    file_name = request.files['audio'].filename

    if file_name == '':
        logging.warn('No files attached. exiting function')
        return None

    if request.method == 'POST':
        # save the single file
        audio = request.files['audio']

        logging.debug('request file: {}'.format(audio.filename))

        abs_path = os.path.join(uploads_dir, audio.filename)
        try:

            audio.save(abs_path)
        except Exception as error:
            logging.error('error saving file {}: '.format(audio.filename))
            abort(404)

        #split the stems from the file
        ausp = AudioSpleeter()
        file_paths = ausp.separate(abs_path)

        """
        TO DO: clean signal from files
        """

        #create paths and filenames
        in_path = file_paths[0]

        if zip_output :
            out_filename = in_path + in_path.split(os.path.sep)[-1]

            #zip the files
            out_filename = zip_folder(in_path, out_filename)

            logging.debug('opening file {} to send'.format(out_filename))
            #make sure to delete the files after streaming

            logging.info('end function {0}'.format('upload'))

            return out_filename
            #return send_file(out_filename, as_attachment=True)
        else:
            return in_path





    


