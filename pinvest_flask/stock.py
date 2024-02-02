from flask import Blueprint, url_for, request, redirect, render_template
import yfinance as yf
from pinvest_flask.db import get_db_connection

bp = Blueprint('stock', __name__, url_prefix='/stock')

@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        stock = request.form['stock_name']
        error = None

        if not stock:
            error = 'Stock name is required.'

        if error is None:
            data = yf.Ticker(stock)
            return render_template('stock/results.html', results=data.info)
        else:
            return redirect(url_for('index'))

    return render_template('stock/search.html')
