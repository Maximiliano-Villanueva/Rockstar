from flask import  Flask#, render_template, abort, request, send_file  # send_from_directory
from dotenv import load_dotenv
import os
#load variables to env
curr_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
load_dotenv(os.path.join(curr_dir,'.env'))

app = Flask(__name__)

