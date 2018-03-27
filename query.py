"""
This file contains all the queries for the news database.
You can add addition queries in this file following this formatted

q#_title: replace # with numerical assign to the query's title
q#: replace # with numerical assign to the query
"""

# Query#1
q1_title = "What are the most popular three articles of all time?"
q1 = ("""
    SELECT articles.title, count(*) AS numviews
    FROM articles
    JOIN log ON log.path
    LIKE concat('/article/', articles.slug, '%')
    WHERE log.status LIKE '%200%'
    GROUP BY articles.title
    ORDER BY numviews DESC
    LIMIT 3;
    """)

# Query#2
q2_title = "Who are the most popular article authors of all time?"
q2 = ("""
    SELECT authors.name, count(*) AS numviews
    FROM articles
    JOIN authors ON articles.author = authors.id
    JOIN log ON concat('/article/', articles.slug) = log.path
    WHERE log.status LIKE '%200%'
    GROUP BY authors.name
    ORDER BY numviews DESC;
    """)

q3_title = "On which days did more than 1% of requests lead to errors?"
q3 = ("""
    SELECT day, percent
    FROM (SELECT day, round((sum(numrequests) / (SELECT count(*)
    FROM log
    WHERE substring(cast(log.time AS text), 0, 11) = day) * 100), 2) AS percent
    FROM (SELECT substring(cast(log.time AS text), 0, 11) AS day,
    count(*) AS numrequests
    FROM log
    WHERE status LIKE '%404%' GROUP BY day) AS percentage_of_error
    GROUP BY day
    ORDER BY percent DESC) AS final_results
    WHERE percent >= 1;
    """)
