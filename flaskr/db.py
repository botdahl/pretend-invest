import os
import click
import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
            host='localhost',
            database='pinvest_db',
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'],
            )
    return connection

def init_app(app):
    app.cli.add_command(init_db_command)

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS stocks_tracked;')
    cursor.execute('''
            CREATE TABLE stocks_tracked (
            id serial PRIMARY KEY,
            stock_name TEXT UNIQUE NOT NULL,
            stock_saved_price DECIMAL NOT NULL);
        ''')

    cursor.execute('''
            INSERT INTO stocks_tracked (stock_name, stock_saved_price)
            VALUES (%s, %s)''',
            ('GME', 14.13))
    
    connection.commit()
    cursor.close()
    connection.close()

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')
