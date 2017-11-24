# Author: Jose Carlos Soto Barco
# Description: Connect to the PostgreSQL database server


import psycopg2
from config import config


def connect():
    """connect to the Postgresql database server"""
    conn = None

    try:
        params = config()

        print('Connecting to the Postgresql database... ')
        conn = psycopg2.connect(**params)

        # create cursor
        cursor = conn.cursor()
        # execute a statement
        print('PostgreSQL database version: ')
        cursor.execute('SELECT version()')

        # display the PostgreSQL database version
        db_version = cursor.fetchone()
        print(db_version)

        # close the communication with Postgresql
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
