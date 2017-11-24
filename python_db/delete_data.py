# Author: Jose Carlos Soto Barco
# Description: Delete Data from Tables

import psycopg2
from config import config


def delete_part(part_id):
    """ delete part by part id """
    sql = """ DELETE FROM parts WHERE part_id = %s"""

    try:
        connection = None
        deleted_rows = 0
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        connection = psycopg2.connect(**params)
        # create a new cursor
        cursor = connection.cursor()
        # execute the UPDATE  statement
        cursor.execute(sql, (part_id,))
        # get the number of updated rows
        deleted_rows = cursor.rowcount
        # Commit the changes to the database
        connection.commit()
        # Close communication with the PostgreSQL database
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()

    return deleted_rows


if __name__ == '__main__':
    deleted_rows = delete_part(10)
    print('The number of deleted rows: ', deleted_rows)