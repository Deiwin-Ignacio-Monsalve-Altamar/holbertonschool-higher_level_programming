#!/usr/bin/python3
import MySQLdb
import sys


def allCitiesState():
    db = MySQLdb.connect(host='localhost', port=3303, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                ON cities.state_id = states.id ORDER BY cities.id ASC")

    dataRows = cur.fetchall()
    for row in dataRows:
        print(row)

    db.close()
    cur.close()


if __name__ == '__main__':
    allCitiesState()
