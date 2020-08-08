#!/usr/bin/python3
"""Exercise
"""
import MySQLdb
import sys


def getallstates():
    """COnect
    """
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC')
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    getallstates()
