#!/usr/bin/python3

"""
Module to list states that match a given name from the database hbtn_0e_0_usa
safe from MySQL injections!
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
    que = """SELECT * FROM states WHERE BINARY name = %s
            ORDER BY id ASC"""
    cur.execute(que, (argv[4],))

    # Obtaining query results.
    query_rows = cur.fetchall()

    # Printing results.
    for row in query_rows:
        print(row)

    # Closing connections.
    cur.close()
    conn.close()
