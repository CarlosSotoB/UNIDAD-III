# Author: Jose Carlos Soto Barco
# Description: the tables are created

import psycopg2
from config import config


def create_tables():
    """Create tables in the Postgresql database"""

    commands = (
        """
        CREATE TABLE log(
        id SERIAL PRIMARY KEY,
        ts TIMESTAMP NOT NULL,
        phrase VARCHAR (128) NOT NULL, 
        letters VARCHAR (32)NOT NULL,
        ip VARCHAR (16) NOT NULL,
        browser_string VARCHAR (256) NOT NULL,
        results VARCHAR (64) NOT NULL)""",
        )
    connection = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        # create table one by one
        for command in commands:
            cursor.execute(command)
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        connection.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    create_tables()