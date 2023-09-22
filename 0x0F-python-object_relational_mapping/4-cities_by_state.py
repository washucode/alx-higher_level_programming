#!/usr/bin/python3

"""
Module to list all states from database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # declaring variables passed.
    db_var = {
        'host': 'localhost',
        'port': 3306,
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3],
        'charset': 'utf8'
    }

    # creating connection to the database.
    conn = MySQLdb.connect(**db_var)
    # Creating a cursor for database manipulation.
    cur = conn.cursor()

    # Executing query.
    que = """SELECT cities.id, cities.name, states.name FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC"""
    cur.execute(que)

    # Obtaining query results.
    query_rows = cur.fetchall()

    # Printing results.
    for row in query_rows:
        print(row)

    # Closing connections.
    cur.close()
    conn.close()
