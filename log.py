#!/usr/bin/env python

import psycopg2


def connect(dbname="news"):
    """Connect to the PostgreSQL database and returns a database connection."""
    try:
        conn = psycopg2.connect("dbname={}".format(dbname))
        c = conn.cursor()
        return conn, c
    except psycopg2.Error as err:
        print("Unable to connect to the database")
        print(err)
        sys.exit(1)


def pop_art():
    """Prints most popular three articles."""
    db, c = connect()
    query = """
    SELECT title,
       views
    FROM
    (SELECT title,
           count(title) AS views
    FROM articles,
         log
    WHERE log.path = concat('/article/', articles.slug)
    GROUP BY title
    ORDER BY views DESC) AS most_popular
    LIMIT 3;"""
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\n###Popular Articles###\n")
    for i in result:
        print("\"" + i[0] + "\"" + " -- " + str(i[1]) + " views")


def pop_auth():
    """Prints most popular article authors of all time."""
    db, c = connect()
    query = """
    SELECT name,
       views
    FROM
   (SELECT authors.name,
          count(articles.author) AS views
   FROM articles,
        log,
        authors
   WHERE log.path = concat('/article/', articles.slug)
     AND articles.author = authors.id
   GROUP BY authors.name
   ORDER BY views DESC) AS pop_authors"""
    c.execute(query)
    result = c.fetchall()
    db.close()
    print("\n###Popular Authors###\n")
    for i in result:
        print("\"" + i[0] + "\"" + " -- " + str(i[1]) + " views")


def log_err():
    """Print days on which more than 1% of browser requests lead to errors"""
    conn, c = connect()
    query = """
    SELECT date, error_percent
    FROM
   (SELECT date(TIME),
          round(100.0*sum(CASE log.status
                              WHEN '200 OK' THEN 0
                              ELSE 1
                          END)/count(log.status), 2) AS error_percent
    FROM log
    GROUP BY date(TIME)
    ORDER BY error_percent DESC) AS log_errors
    WHERE error_percent > 1.0;"""
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
