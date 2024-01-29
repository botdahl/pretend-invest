from flask import Blueprint, url_for

from pinvest_flask.db import get_db_connection

bp = Blueprint('stock', __name__, url_prefix='/stock')
