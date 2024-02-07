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

    cursor.execute('DROP TABLE IF EXISTS portfolio;')
    cursor.execute('''
            CREATE TABLE portfolio (
            id serial PRIMARY KEY,
            name TEXT NOT NULL,
            balance INTEGER NOT NULL);
        ''')

    cursor.execute('DROP TABLE IF EXISTS stock;')
    cursor.execute('''
            CREATE TABLE stock (
            id serial PRIMARY KEY,
            portfolio_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            price DECIMAL NOT NULL,
            amount INTEGER NOT NULL);
        ''')

    cursor.execute('''
            INSERT INTO portfolio (name, balance)
            VALUES (%s, %s)''',
            ('TEST', 100000))

    cursor.execute('''
            INSERT INTO stock (portfolio_id, name, price, amount)
            VALUES (%s, %s, %s, %s)''',
            (1, 'GME', 14.3, 10))
    
    connection.commit()
    cursor.close()
    connection.close()

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')
