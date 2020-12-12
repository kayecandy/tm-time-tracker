from flask import session, request
from app import app
from src.models.user import User

@app.route('/api/login', methods=['POST'])
def api_login():
    
    u = User.login(request.form['username'], request.form['password'])

    if u is None:
        return {'message': 'Incorrect username/password'}, 401

    session['user'] = u
    return {'message': 'Login success!'}, 200


@app.route('/api/logout', methods=['POST'])
def api_logout():
    session.clear()
    return {'message': 'Logout success!'}, 200