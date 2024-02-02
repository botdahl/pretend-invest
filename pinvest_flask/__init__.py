import os
from flask import Flask, render_template

def create_app(test_config=None):
    from . import db
    from . import stock

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
            SECRET_KEY='dev',
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
        cursor.execute('SELECT * FROM stocks_tracked;')
        stocks_tracked = cursor.fetchall()
        cursor.close()
        connection.close()

        return render_template('index.html', stocks_tracked=stocks_tracked)

    db.init_app(app)

    app.register_blueprint(stock.bp)

    return app
