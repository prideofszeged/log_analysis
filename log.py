#!/usr/bin/env python

import psycopg2


def connect(dbname="news"):
    """Connect to the PostgreSQL database and returns a database connection."""
    try:
        conn = psycopg2.connect("dbname={}".format(dbname))
        c = conn.cursor()
        return conn, c
    except:
        print("Connection failed")


def pop_art():
    """Prints most popular three articles."""
    db, c = connect()
    query = "select * from popular_articles limit 3"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\nPopular Articles:\n")
    for i in result:
        print("\"" + i[0] + "\"" + " -- " + str(i[1]) + " views")


def pop_auth():
    """Prints most popular article authors of all time."""
    db, c = connect()
    query = "select * from popular_authors"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\nPopular Authors:\n")
    for i in result:
        print("\"" + i[0] + "\"" + " -- " + str(i[1]) + " views")


def log_err():
    """Print days on which more than 1% of browser requests lead to errors"""
    conn, c = connect()
    query = "select * from log_errors where error_percent > 1.0"
    c.execute(query)
    result = c.fetchall()
    conn.close()
    print("\nDays with more than 1% of errors:\n")
    for i in result:
        print(i[0].strftime('%B %d, %Y') + ' -- ' + str(i[1]) + '% errors')


if __name__ == '__main__':
    pop_art()
    pop_auth()
    log_err()
    print("\nDone\n")
