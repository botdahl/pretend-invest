import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    connection = psycopg2.connect(
            host='localhost',
            database='pinvest_db',
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM stock_tracked;')
    stocks = cursor.fetchall()
    cursor.close()

    return render_template('index.html', stocks=stocks)
