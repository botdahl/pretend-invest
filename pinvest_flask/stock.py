from flask import Blueprint, url_for, request, redirect, render_template
import yfinance as yf
import psycopg2
from pinvest_flask.db import get_db_connection

bp = Blueprint('stock', __name__, url_prefix='/stock')

@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        if 'stock_name' in request.form:
            stock = request.form['stock_name']
            data = yf.Ticker(stock)
            return render_template('stock/results.html', results=data.info)

        else:
            return redirect(url_for('index'))

    return render_template('stock/search.html')

@bp.route('/buy', methods=('GET', 'POST'))
def buy():
    if request.method == 'POST':
        if 'stock_buy_name' in request.form:
            stock = request.form['stock_buy_name']
            price = request.form['stock_buy_price']

            try:
                connection = get_db_connection()
                cursor = connection.cursor()
                cursor.execute('''
                       INSERT INTO stocks_tracked (stock_name, stock_saved_price)
                       VALUES (%s, %s)''',
                       (stock, price))
                connection.commit()
                cursor.close()
                connection.close()
                print('end')
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    return redirect(url_for('stock.search'))

@bp.route('/<int:id>/delete', methods=('GET', 'POST'))
def delete(id):
    try:
        print(id)
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM stocks_tracked WHERE id = '%s'" % (id,))

        connection.commit()
        cursor.close()
        connection.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return redirect(url_for('index'))
