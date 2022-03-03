from flask import  Flask, render_template, abort, request, send_file
from app import app
from main import uploads_dir
import os
from AudioSpleetc import AudioSpleeter
from functions import *

from AppLoger import AppLoger

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
    logging.info('entering function: {0}'.format('upload'))

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
        out_filename = in_path + in_path.split(os.path.sep)[-1]

        #zip the files
        out_filename = zip_folder(in_path, out_filename)

        logging.debug('opening file {} to send'.format(out_filename))
        #make sure to delete the files after streaming

        logging.info('end function {0}'.format('upload'))
        return send_file(out_filename, as_attachment=True)
        
    abort(404)