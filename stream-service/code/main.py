
import os
import app
from AppLoger import AppLoger
#from asset_handler import AssetHandler
#from asset_handlers.db_writer import MysqlConnector
import pathlib
import uuid

# Tornado web server
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


if __name__ == '__main__':
    """
    create uploads folder and init app
    """

    music_dir = os.path.join(pathlib.Path().resolve(), 'music')
    os.environ['music_dir'] = music_dir
    os.environ['ROOT_DIR'] = os.path.dirname(os.path.abspath(__file__))
    #create logger
    uuid_session = os.getenv("app_guid")
    app_name = os.getenv("APP_NAME")
    AppLoger.create_logger(guid = str(uuid_session), log_name = app_name)

    logger = AppLoger.getLogger(str(uuid_session))
    
    """
    create asset handler
    """
    """
    db_conn = MysqlConnector(host = os.getenv("MYSQL_HOST"), user = os.getenv("MYSQL_USER"), password = os.getenv("MYSQL_PASSWORD"), database = os.getenv("MYSQL_DB"), logger = logger)
    AssetHandler.logger = logger
    AssetHandler.setHandler(db_conn)
    """
    host = os.getenv("FLASK_HOST")
    port = os.getenv("FLASK_PORT")
    debug = os.getenv("FLASK_DEBUG")
    #import the routing page
    import app.view
    #init server with .env conf
    #app.app.run(host = host, port=port, debug=debug)
    if __name__ == '__main__':
        http_server = HTTPServer(WSGIContainer(app.app))
        http_server.listen(port)
        IOLoop.instance().start()

