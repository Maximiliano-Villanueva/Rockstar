import json
from flask import Flask,render_template, Response, jsonify, request, abort
import sys

from asset_handler import AssetHandler
from app import app
import os
from glob import glob

CODE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(CODE_DIR)

from AppLoger import AppLoger

#get app loger
app_guid = os.environ.get('app_guid', 'temp-log')
logging = AppLoger.getLogger(app_guid)

#simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    logging.info('routing to: {0}'.format('index'))
    return render_template('index.html')

@app.route('/songs', methods=['GET'])
def get_songs():
    
    logging.info('routing to: {0}'.format('get_songs'))
    
    rootdir = os.environ.get('ROOT_DIR')
    """
    results = glob(os.path.join(rootdir, 'music', 'uploads', '*'))
    results =[os.path.basename(r) for r in results]
    """
    results = AssetHandler.read(path = os.path.join(rootdir, 'music', 'uploads'), filter = '*')
    return jsonify(results)

@app.route('/play/<string:stream_id>')
def stream_music(stream_id):
    buffer_size = 1024
    
    rootdir = os.environ.get('ROOT_DIR')
    song_path = os.path.join(rootdir, 'music', 'uploads', stream_id)
    file_ext = song_path.split('.')[-1]

    def stream_helper_func():
        
        if not os.path.exists(song_path):
            abort(404)
        
        with open(song_path, 'rb') as song:
            data = song.read(buffer_size)
            
            while data:
                yield data
                data = song.read(buffer_size)

    return Response(stream_helper_func(), mimetype="audio/"+file_ext)






    


