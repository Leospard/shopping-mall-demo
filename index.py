# -*- coding: utf-8 -*-
import logging
from re import S
import pymysql
import os, hashlib

logger = logging.getLogger()

conn = None

# initialize hook, connect to the database
def initialize(context):
    global conn
    try:
        conn = pymysql.connect(
            # Replace it with your host name.
            host=os.environ['MYSQL_ENDPOINT'],
            # Replace it with your port number.
            port=int(os.environ['MYSQL_PORT']),
            # Replace it with your username.
            user=os.environ['MYSQL_USER'],
            # Replace the  password with the one corresponding to your username.
            passwd=os.environ['MYSQL_PASSWORD'],
            # Replace it with the name of your database.
            db=os.environ['MYSQL_DBNAME'],
            connect_timeout=5)
    except Exception as e:
        logger.error(e)
        logger.error(
            "ERROR: Unexpected error: Could not connect to MySql instance.")
        raise Exception(str(e))


def pre_stop(context):
    logger.info("pre_stop hook start.")
    if conn != None:
        conn.close()
    logger.info("pre_stop hook finish.")

def handler(event, context):
    if conn is None:
        raise Exception("Mysql connection not initialized.")

    # Check if the server is alive.
    # If the connection is closed, reconnect.
    conn.ping(reconnect=True)
    try:
        # Create table
        # conn.execute('''CREATE TABLE users 
        #         (userId INTEGER PRIMARY KEY, 
        #         password TEXT,
        #         email TEXT,
        #         firstName TEXT,
        #         lastName TEXT,
        #         phone TEXT
        #         )''')

        # conn.execute('''CREATE TABLE products
        #         (productId INTEGER PRIMARY KEY,
        #         name TEXT,
        #         price REAL,
        #         description TEXT,
        #         image TEXT,
        #         stock INTEGER,
        #         categoryId INTEGER,
        #         FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
        #         )''')

        # conn.execute('''CREATE TABLE kart
        #         (userId INTEGER,
        #         productId INTEGER,
        #         num INTEGER,
        #         FOREIGN KEY(userId) REFERENCES users(userId),
        #         FOREIGN KEY(productId) REFERENCES products(productId)
        #         )''')

        # conn.execute('''CREATE TABLE categories
        #         (categoryId INTEGER PRIMARY KEY,
        #         name TEXT
        #         )''')

        # conn.execute('''CREATE TABLE orders
        #         (orderId INTEGER PRIMARY KEY,
        #         userId INTEGER,
        #         productId INTEGER,
        #         num INTEGER
        #         )''')
        cur = conn.cursor()
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (1, 'Men\'s'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (2, 'Women\'s'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (3, 'HeadPhones'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (4, 'Computers'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (5, 'CellPhones'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (6, 'Snacks'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (7, 'Drinks'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (8, 'CookedFoods'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (9, 'Basketball'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (10, 'Tennis'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (11, 'Golf'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (12, 'Clothing'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (13, 'Camping'))
        cur.execute('''INSERT INTO categories (categoryId, name) VALUES (?, ?)''', (14, 'Cycling'))
        password = '12345678'
        email = '1023553676@qq.com'
        firstName = 'Admin'
        lastName = 'Tony'
        phone = '10101010'
        cur.execute('''INSERT INTO users (password, email, firstName, lastName, phone) VALUES (?, ?, ?, ?, ?)''', (hashlib.md5(password.encode()).hexdigest(), email, firstName, lastName, phone))
        password = '12345678'
        email = '1354178359@qq.com'
        firstName = 'Admin2'
        lastName = 'Ben'
        phone = '1010101'
        cur.execute('''INSERT INTO users (password, email, firstName, lastName, phone) VALUES (?, ?, ?, ?, ?)''',
                    (hashlib.md5(password.encode()).hexdigest(), email, firstName, lastName, phone))
        conn.commit()

        return 
    except Exception as e:
        logger.error(
            "ERROR: Unexpected error: Could not connect to MySql instance.")
        raise Exception(str(e))
