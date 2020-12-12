from flask import request
from app import route_api, app

from src.models.tag import Tag

@app.route('/api/tags/search', methods=['GET', 'POST'])
@route_api()
def api_tags_search():
    return {
        'tags': Tag.search(request.values['q'])
    }
