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
    connection = get_db_connection
    cursor = connection.cursor()
    cursor.execute(open('schema.sql', 'r').read())
    
    connection.commit()
    cursor.close()
    connection.close()

@click.command('init-db')
def init_db_command():
    init_db()
    click.echo('Initialized the database.')
