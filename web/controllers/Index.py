from flask import Blueprint
from flask import render_template
from application import app
from flask import request


index_route = Blueprint('index_page', __name__)


@index_route.route('/')
@index_route.route('/index')
def index():
    app.logger.debug(request.path)
    return render_template('index.html')
