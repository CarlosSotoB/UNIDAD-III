# Author: Jose Carlos Soto Barco
# Description: Update Data in a Table

import psycopg2
from config import config


def update_vendor(vendor_id, vendor_name):
    """ update vendor name based on the vendor id"""
    sql = """ UPDATE vendors
                SET vendor_name = %s 
                WHERE vendor_id = %s """
    try:
        connection = None
        updated_rows = 0

        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        cursor.execute(sql, (vendor_name, vendor_id))
        updated_rows = cursor.rowcount
        connection.commit()
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:

            connection.close()
    return updated_rows


if __name__ == '__main__':
    update_vendor(48, '3M Corp')

