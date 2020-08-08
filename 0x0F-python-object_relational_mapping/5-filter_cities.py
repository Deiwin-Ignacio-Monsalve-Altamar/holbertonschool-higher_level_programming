#!/usr/bin/python3
"""Write a script that takes
"""
import MySQLdb
import sys


def allCitiesState():
    """takes in the name of a state
    """
    db = MySQLdb.connect(port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                ON cities.state_id = states.id \
                WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    dataRow = cur.fetchall()

    listData = []
    for name in dataRow:
        listData.append(name[0])

    print(', '.join(listData))

    db.close()
    cur.close()


if __name__ == '__main__':
    allCitiesState()
