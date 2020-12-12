import os
from functools import wraps
from flask import Flask, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import json


# Load env
load_dotenv(override=True)



# Init App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY', 'tm-time-tracker')
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=bool(int(os.getenv('FLASK_DEBUG', 0))))


# APIs
def route_api():
    def _route_api(f):
        @wraps(f)
        def __route_api(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                if bool(int(os.getenv('FLASK_DEBUG', 0))):
                    if  'raw' in request.form or 'raw' in request.args:
                        raise e

                return {
                    'status': 'error',
                    'message': str(e)
                }, e.code if hasattr(e, 'code') else 500
        
        return __route_api

    return _route_api



# Routes
import routes