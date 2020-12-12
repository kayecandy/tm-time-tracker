from flask import request
from app import route_api, app
from src.api.user import current_user_only, loggedin_only
from src.models.checkin import CheckIn


@app.route('/api/checkin/add', methods=['POST'])
@route_api()
@loggedin_only()
def api_checkin_add():
    checkin = CheckIn(
        hours=request.form['hours'], 
        tag_id=request.form['tag_id'] if 'tag_id' in request.form else None, 
        tag_name=request.form['tag_name'] if 'tag_name' in request.form else None,
        activity=request.form['activity']
    )

    checkin.add()
    return {
        'message': 'Successfully added checkin',
        'checkin': checkin
    }


@app.route('/api/checkin/delete', methods=['POST'])
@route_api()
@current_user_only(lambda req: CheckIn.verify_user_id(req.form['checkin_id']))
def api_checkin_delete(checkin:CheckIn):
    checkin.delete()
    return {
        'message': 'Checkin successfully deleted',
        'checkin': checkin
    }