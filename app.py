from flask import Flask, app, config,make_response,jsonify
from flask.globals import request, session
from flask.templating import render_template
import jwt
import datetime 
from datetime import timedelta
from functools import wraps
import uuid

from models.Users import Users
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


app.config['SECRET_KEY'] = "499baae0-223a-4e68-b72e-eb0719d0ee37"

# def token_required(func):
#     @wraps(func)
#     def decorated(*args, **kwrags):
#         token = request.args.get('token')
#         print("---------token-",token)
#         if not token:
#             return jsonify({'Token is missing'})
#         try:
#             payload = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
#             print("payload-----",payload)
#         except:
#             return jsonify({"Invalid token"})
        
#         # return func(*args, **kwrags)
#     return decorated


@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/login')
def login():
    auth= request.authorization
    print("--auth.username, auth.password--",auth.username, auth.password)
    if not auth or not auth.username or not auth.password:
       return make_response(
                    'Could not verify auth',
                    401,
                    {'WWW-Authenticate' : 'Basic realm ="Login Required !!"'}
                ) 
    else:
        # print (generate_password_hash("akshay", "sha256"))
        hash_pwd = generate_password_hash(auth.password, "sha256")
        print("---hash_pwd--",hash_pwd)
        user = Users()
        respon =  user.login(auth.username, auth.password)
        # print("respon0--",respon['password'])
        # print("respon0--",respon,auth.password)
        if respon is None:
            return make_response(
                    'Could not verify login',
                    401,
                    {'WWW-Authenticate' : 'Basic realm ="Login Required !!"'}
                ) 
        
        if check_password_hash(respon['password'],auth.password):
            token = jwt.encode({'id':respon['id'], 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])
            print("token---", token)

            return jsonify({'token':token.decode('UTF-8')})
        else:
            print("check_password_hash---")
            return make_response(
                    'Could not verify hash',
                    401,
                    {'WWW-Authenticate' : 'Basic realm ="Login Required !!"'}
                ) 

@app.route('/register')
def register():
    return render_template('register.html')
    
if __name__ == '__main__':
    app.run(debug=True)
    