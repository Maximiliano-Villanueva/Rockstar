from flask import  Flask#, render_template, abort, request, send_file  # send_from_directory
from dotenv import load_dotenv
import os
import uuid
#load variables to env
curr_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
load_dotenv(os.path.join(curr_dir,'.env'))

uuid_session = uuid.uuid4()
#os.environ['app_guid_session'] = uuid_session
os.environ['app_guid'] = str(uuid_session)



app = Flask(__name__)

