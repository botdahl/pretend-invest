import os
from . import db

from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, ''),
            )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        connection = db.get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM stock_tracked;')
        stocks_tracked = cursor.fetchall()
        cursor.close()
        connection.close()

        return render_template('index.html', stocks_tracked=stocks_tracked)


    db.init_app(app)

    return app
