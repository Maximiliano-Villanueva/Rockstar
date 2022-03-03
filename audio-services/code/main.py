
import os
import app
from AppLoger import AppLoger

import pathlib
import uuid




uploads_dir = os.path.join(pathlib.Path().resolve(), 'uploads')

if __name__ == '__main__':
    """
    create uploads folder and init app
    """
    #create logger
    uuid_session = uuid.uuid4()
    app_name = os.getenv("APP_NAME")
    #os.environ['app_guid_session'] = uuid_session
    os.environ['app_guid'] = str(uuid_session)
    AppLoger.create_logger(guid = str(uuid_session), log_name = app_name)

    #create upload dir
    try:
        os.makedirs(uploads_dir)
    except:
        pass
    
    host = os.getenv("FLASK_HOST")
    port = os.getenv("FLASK_PORT")
    debug = os.getenv("FLASK_DEBUG")
    #import the routing page
    import app.view
    #init server with .env conf
    app.app.run(host = host, port=port, debug=debug)

