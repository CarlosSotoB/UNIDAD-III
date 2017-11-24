# Author: Jose Carlos Soto Barco
# Description: transaction the data

import psycopg2
from config import config


def add_part(part_name, vendor_list):
    # statement for inserting a new row into the parts table
    insert_part = """INSERT INTO parts(part_name) VALUES (%s) RETURNING part_id"""
    # statement for inserting a new row into the vendors table
    assign_vendor = """INSERT INTO vendor_parts(vendor_id,
                        part_id) VALUES (%s, %s)"""

    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        # insert a new part
        cursor.execute(insert_part, (part_name,))
        # get the part id
        part_id = cursor.fetchone()[0]
        # assign part provide by vendors
        for vendor_id in vendor_list:
            cursor.execute(assign_vendor, (vendor_id, part_id))
        # commit changes
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    add_part('SIM Tray', (48, 49))
    add_part('speaker', (50, 51))
    add_part('Vinbrator', (52, 53))
    add_part('Home Button', (48, 53))
    add_part('LTE Modem', (48, 53))