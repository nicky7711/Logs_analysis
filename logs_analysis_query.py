#! /usr/bin/env python
"""
Created on Thu Nov  2 19:10:39 2017

@author: Nicholas
"""


import psycopg2


DB_NAME = "news"
query1 = "SELECT articles.title,count(*) as num FROM articles,log WHERE log.path=CONCAT('/article/',articles.slug) GROUP BY articles.title ORDER BY num DESC LIMIT 3;"  # noqa
query2 = "SELECT authors.name, count(*) AS views FROM articles INNER JOIN authors ON articles.author = authors.id INNER JOIN log ON log.path = concat('/article/', articles.slug) WHERE log.status like '%200%' GROUP BY authors.name ORDER BY views DESC"  # noqa
query3 = """SELECT total.day, ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent 
            FROM (SELECT cast(time as date) as day, count(*) AS error_requests FROM log WHERE status LIKE '404%' GROUP BY day) AS errors
            JOIN (SELECT cast(time as date) as day, count(*) AS requests FROM log GROUP BY day) AS total
            ON total.day = errors.day
            WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
            ORDER BY percent DESC;
        """  # noqa


def request(query):
    ''' Makes a query to the news database '''
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


def print_answer(answer):
    for row in answer:
        print (row[0])

answer1 = request(query1)
answer2 = request(query2)
answer3 = request(query3)

print ("What are the most popular three articles of all time?")
print_answer(answer1)
print ("Who are the most popular article authors of all time?")
print_answer(answer2)
print ("On which days did more than 1% of requests lead to errors?")
print_answer(answer3)
