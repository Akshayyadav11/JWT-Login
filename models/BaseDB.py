# import MySQLdb
import mysql.connector
import json
import uuid

class BaseDB:
    def __init__(self) :
        with open('dbconfig.json') as f:        
            self.config = json.load(f)
    
    def connect(self):
          
        
        
        dbConnection =  mysql.connector.connect(host = self.config['MYSQL_HOST'],
                            user = self.config['MYSQL_USER'],
                            passwd = self.config['MYSQL_PASSWORD'],
                            db = self.config['MYSQL_DB']
                           )

        return dbConnection
    def get_connection(self):
        conn = self.connect()
        return conn
