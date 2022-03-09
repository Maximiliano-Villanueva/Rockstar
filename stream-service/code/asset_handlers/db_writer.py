import mysql.connector
from Abstrac_Handler import AbstractHandler

@AbstractHandler.register
class MysqlConnector(AbstractHandler):
    """
    mysql connector handler for CRUD operations
    """

    def __init__(self, host = None, user = None, password = None, database = None):
        """
        basic connection
        """
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        AbstractHandler.__init__(self)

    def write(self, **kargs):
        """
        execute sql command
        example: "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = [
                ('Peter', 'Lowstreet 4'),
                ('Amy', 'Apple st 652')
            ]
        """
        logging = self.logging
        #validate params
        requested_params = ['query']

        if not self.validateParameter(parameter = requested_params, param_list = kargs):
            logging.error('error calling function {0}, missing parameters'.format('write'))
            raise Exception('parameters {0} are required'.format(str(requested_params)))
        
        query = kargs['query']
        values = kargs['values'] if 'values' in kargs.keys() else None

        logging.info('entering function execute')

        cursor = self.db.cursor()

        logging.debug('cursor opened')

        if values is None:
            cursor.execute(query)

        else:
            cursor.execute(query, values)
        
        logging.debug('query: {0}. Values : {1}'.format(query, str(values)))
        logging.info('leaving function execute')   

        self.db.commit()
    
    def get(self, **kargs):
        """
        execute sql command
        """
        logging = self.logging
        #validate params
        requested_params = ['query']

        if not self.validateParameter(parameter = requested_params, param_list = kargs):
            logging.error('error calling function {0}, missing parameters'.format('write'))
            raise Exception('parameters {0} are required'.format(str(requested_params)))

        query = kargs['query']

        logging.info('entering function select')

        cursor = self.db.cursor()

        logging.debug('cursor opened')

        cursor.execute(query)
        
        res = cursor.fetchall()
        
        logging.debug('query: {0}'.format(query))
        logging.info('leaving function select')   

        return res



a = MysqlConnector(host = "db-music", user = 'user', password = 'password', database='audio_service')
a.write("INSERT INTO song (title) values ('test')")
    