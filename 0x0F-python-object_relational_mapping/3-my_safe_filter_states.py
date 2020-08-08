#!/usr/bin/python3
"""do you remember the previous task? 
"""
import MySQLdb
import sys


def inyeccionSQL():
    """you test "Arizona'
    """
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states \
                WHERE name=%s \
                ORDER BY id ASC", (sys.argv[4],))
    for row in cur.fetchall():
        if row[1] == sys.argv[4]:
            print(row)

    db.close()
    cur.close()


if __name__ == '__main__':
    inyeccionSQL()
