from functools import wraps
from flask import render_template, session,jsonify, redirect, url_for
from app import app

# API - User
import src.api.user


def login_redirect():
    def _login_redirect(f):
        @wraps(f)
        def __login_redirect(*args, **kwargs):
            if session.get('user') is None:
                return redirect(url_for('login'))
            
            return f(*args, **kwargs)

        return __login_redirect
    return _login_redirect





# Views
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/')
@login_redirect()
def index():
    return render_template('index.html')
