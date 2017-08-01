#!/usr/bin/env python
import psycopg2


RESULTS = []

TITLES = []

# 1. What are the most popular three articles of all time?

QUERY1 = '''SELECT title , views FROM articleView limit 3;'''


# 2. Who are the most popular article authors of all time?

QUERY2 = '''SELECT au.name , sum(views) as Views FROM articleView
            JOIN authors au on au.id = articleView.author
            GROUP BY au.name
            ORDER BY Views desc;'''

# 3. On which days did more than 1% of requests lead to errors?

QUERY3 = '''SELECT * FROM
            (
            SELECT date(time)  ,
            round(((Failed.fstatus * 100.0) / count(log.status) )  , 2 )
             AS percentage   FROM log
            JOIN (
                    SELECT date(f.time) as fdate ,
                            count(f.status) as fstatus FROM log f
                    WHERE f.status = '404 NOT FOUND'
                    GROUP BY date(f.time)
            ) Failed
            on failed.fdate = date(time)
            GROUP BY date(time) , Failed.fstatus) ss
            WHERE percentage  > 1;'''


def getquery(num):
    ''' Return Query that should be returned
        according to the num paramter passed '''
    if num == 1:
        return QUERY1
    elif num == 2:
        return QUERY2
    return QUERY3


def gettitle(num):
    ''' Return the title as header of the question
        to be displayed later '''
    if num == 1:
        return 'What are the most popular three articles of all time?'
    elif num == 2:
        return 'Who are the most popular article authors of all time?'
    return 'On which days did more than 1% of requests lead to errors?'


def runquery(num):
    ''' Get and run the query on the db and store the data in RESULTS
        variable to be displayed later '''

    database = psycopg2.connect('dbname=news')
    cur = database.cursor()
    query = getquery(num)
    cur.execute(query)
    rows = cur.fetchall()
    TITLES.append(gettitle(num))
    RESULTS.append(rows)


def printoutput():
    ''' Print out the results that have been ran on the db
        and stored earlier on RESULTS variable '''

    for num in range(0, len(RESULTS)):
        result = ""
        print "\n"
        print str(num+1) + " - " + str(TITLES[num])
        print "\n"

        for row in list(RESULTS[num]):
            for value in range(0, len(row)):
                if value != len(row) - 1:
                    result += str(row[value]) + " , "
                else:
                    if num == 2:
                        result += str(row[value]) + '%'
                    else:
                        result += str(row[value]) + " VIEWS"
            print result
            result = ""

runquery(1)
runquery(2)
runquery(3)
printoutput()
