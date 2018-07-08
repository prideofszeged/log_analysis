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
    query = "select title, views from (select title, count(title) as views from\
    articles, log where log.path = concat('/article/',articles.slug) group by\
    title order by views desc) as most_popular limit 3;"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\n###Popular Articles###\n")
    for i in result:
        print("\"" + i[0] + "\"" + " -- " + str(i[1]) + " views")


def pop_auth():
    """Prints most popular article authors of all time."""
    db, c = connect()
    query = "select name, views from (select authors.name, \
    count(articles.author) as views from articles, log, authors where \
    log.path = concat('/article/',articles.slug) and articles.author = \
    authors.id group by authors.name order by views desc) as pop_authors;"
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\n###Popular Authors###\n")
    for i in result:
        print("\"" + i[0] + "\"" + " -- " + str(i[1]) + " views")


def log_err():
    """Print days on which more than 1% of browser requests lead to errors"""
    conn, c = connect()
    query = "select date, error_percent from \
    (select date(time),round(100.0*sum(case log.status when '200 OK' then \
    0 else 1 end)/count(log.status),2) as error_percent from log group \
    by date(time) order by error_percent desc) as log_errors where\
    error_percent > 1.0;"
    c.execute(query)
    result = c.fetchall()
    conn.close()
    print("\n###Days with more than 1% of errors###\n")
    for i in result:
        print(i[0].strftime('%B %d, %Y') + ' -- ' + str(i[1]) + '% errors')


if __name__ == '__main__':
    pop_art()
    pop_auth()
    log_err()
    print("\nDone\n")
