import os
import psycopg2

connection = psycopg2.connect(
        host="localhost",
        database="pinvest_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'],
        )

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS stock_tracked;')

cursor.execute('''CREATE TABLE stock_tracked (
               id serial PRIMARY KEY,
               stock_name varchar(30),
               stock_buying_price decimal,
               stock_selling_price decimal,
               stock_current_price decimal
               );''')

cursor.execute(
        'INSERT INTO stock_tracked (stock_name, stock_buying_price, stock_current_price)'
        'VALUES (%s, %s, %s)',
        ('GME', 14.49, 14.49)
        )

connection.commit()
cursor.close()
connection.close()
