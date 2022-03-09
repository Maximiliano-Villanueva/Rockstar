import mysql.connector

class MysqlConnector:
    """
    mysql connector handler for CRUD operations
    """

    def __init__(self, host = None, user = None, password = None, database = None, logger = None):
        """
        basic connection
        """
        self.db = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )

        self.logger = logger

    def write(self, query, values = None):
        """
        execute sql command
        example: "INSERT INTO customers (name, address) VALUES (%s, %s)"
        val = [
                ('Peter', 'Lowstreet 4'),
                ('Amy', 'Apple st 652')
            ]
        """
        logger = self.logger
        if logger is not None:
            logger.info('entering function execute')

        cursor = self.db.cursor()

        if logger is not None:
            logger.debug('cursor opened')

        if values is not None:
            cursor.execute(query)

        else:
            cursor.execute(query, values)
        
        
        if logger is not None:
            logger.debug('query: {0}. Values : {1}'.format(query, values))
            logger.info('leaving function execute')   

        self.db.commit()
    
    def get(self, query):
        """
        execute sql command
        """
        logger = self.logger
        if logger is not None:
            logger.info('entering function select')

        cursor = self.db.cursor()

        if logger is not None:
            logger.debug('cursor opened')

        cursor.execute(query)
        
        res = cursor.fetchall()
        
        if logger is not None:
            logger.debug('query: {0}'.format(query))
            logger.info('leaving function select')   

        return res



a = MysqlConnector(host = "db-music", user = 'user', password = 'password', database='audio_service')
a.write("INSERT INTO song (title) values ('test')")
    