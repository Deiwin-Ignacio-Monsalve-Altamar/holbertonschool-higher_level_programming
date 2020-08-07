#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def getallstates():
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC')
    dataRow = cur.fetchall()
    for row in dataRow:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    getallstates()
