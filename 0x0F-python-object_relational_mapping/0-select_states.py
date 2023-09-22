#!/usr/bin/python3

"""
Module that contains a script that lists all states from the database
hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db_options = {
        "host": "localhost",
        "port": 3306,
        "user": argv[1],
        "password": argv[2],
        "database": argv[3],
        "charset": "utf8"
    }

    # Connect to a MySQL database based on command line arguments
    conn = MySQLdb.connect(**db_options)

    # Create cursor to execute queries and use dictionary format
    cursor = conn.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and store in variable
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    conn.close()
