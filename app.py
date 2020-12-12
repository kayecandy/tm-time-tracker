import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


# Load env
load_dotenv(override=True)



# Init App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI', '')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.cmonfig['SECRET_KEY'] = os.getenv('SESSION_SECRET_KEY', 'tm-time-tracker')
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=bool(int(os.getenv('FLASK_DEBUG', 0))))


# Routes
import routes