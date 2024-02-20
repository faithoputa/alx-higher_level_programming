#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to a MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1], # mysql username
        passwd=sys.argv[2], # mysql password
        db=sys.argv[3] # database name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all records
    rows = cursor.fetchall()

    # Print each record
    for row in rows:
        print(row)

    # Close the cursor and the database
    cursor.close()
    db.close()

