from functools import wraps
from flask import session, request
from app import app, route_api
from src.models.user import User


def loggedin_only():
    def _loggedin_only(f):
        @wraps(f)
        def __loggedin_only(*args, **kwargs):
            if session.get('user') is None:
                return {
                    'status': 'error',
                    'message': 'Unauthorized'
                }, 401

            return f(*args, **kwargs)
        
        return __loggedin_only

    return _loggedin_only


def current_user_only(get_userid):
    def _current_user_only(f):
        @wraps(f)
        @loggedin_only()
        def __current_user_only(*args, **kwargs):
            obj = get_userid(request)
            if session.get('user')['id'] != obj[0]:
                return {
                    'status': 'error',
                    'message': 'Invalid operation'
                }, 403

            
            return f(obj[1], *args, **kwargs)

        return __current_user_only
    
    return _current_user_only

@app.route('/api/login', methods=['POST'])
@route_api()
def api_login():
    
    u = User.login(request.form['username'], request.form['password'])

    if u is None:
        return {'message': 'Incorrect username/password'}, 401

    session['user'] = u
    return {'message': 'Login success!'}, 200


@app.route('/api/logout', methods=['POST'])
@route_api()
def api_logout():
    session.clear()
    return {'message': 'Logout success!'}, 200