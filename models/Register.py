from flask import Flask, render_template, request, redirect, url_for, session, Blueprint
from flask_mysqldb import MySQL
from models.BaseDB  import BaseDB  
import re

class Register(BaseDB):    
    def __init__(self):
        self.db = BaseDB()
        print("----",self.db)
    
    
    def register(self, email, username, password):
        try:
            print("----email, username, password-----",email, username, password)
            connection = self.db.get_connection()
            cursor = connection.cursor(dictionary=True)

            cursor.execute('SELECT * FROM accounts WHERE email = %s', (email, ))
            account = cursor.fetchone()
            print("---------",account)
            if account:
                msg = 'Account already exists !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers !'
            elif not username or not password or not email:
                msg = 'Please fill out the form !'
            
            else:
                cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email, ))
                connection.commit()
                msg = 'You have successfully registered !'
            print("msg--",msg)
            
            return msg
        except Exception as e:
            print(e)