from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
from flask_mysqldb import MySQL
from models.BaseDB  import BaseDB  
import re

class Users(BaseDB):    
    def __init__(self):
        self.db = BaseDB()
        print("----",self.db)
    
    def login(self, user):
        try:
            msg = ''
            connection = self.db.get_connection()
            cursor = connection.cursor(dictionary=True)
            query = 'SELECT * FROM accounts WHERE username = %s'
            cursor.execute(query, (user, ))
            print((query, (user,  )))
            account = cursor.fetchone()
           
            print("account----",account)
            return account
        except Exception as e:
            print(e)

    