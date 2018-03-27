#!/usr/bin/python3
import psycopg2
import query

# Name of the database
DATABASE_FILE = "news"

def connect_to_database():
    """
    - Take name of database
    - Connect with database
    - Connect cursor to it
    - Return database and cursor
    """
    db = psycopg2.connect("dbname={}".format(DATABASE_FILE))
    c = db.cursor()
    return db, c
    db.close()

def get_query(query):
    """
    - Take connection to database and cursor
    - Use cursor to query database
    - Close connection of both database and cursor
    - Return query results
    """
    db, c = connect_to_database()
    print("Getting Query...")
    c.execute(query)
    result = c.fetchall()
    db.close()
    c.close()
    return result


def print_formatted_query(question, results):
    """
    - Take output of query from database
    - Print out formatted readable text
    """
    print(question)
    for msg in results:
        print("    " + str(msg[0]) + " -- " + str(msg[1]) + " views")
    print()

def print_formatted_percent_query(question, results):
    """
    - Take output of query from database
    - Print out formatted readable text
    """
    print(question)
    for msg in results:
        print("    " + str(msg[0]) + " -- " + str(msg[1]) + " errors")
    print()

if __name__ == "__main__":
    # Assigns list of results
    q1_query = get_query(query.q1)
    q2_query = get_query(query.q2)
    q3_query = get_query(query.q3)
    print("Queries Complete\n")

    # Show output of formatted query results
    print("Query Results:")
    print_formatted_query(query.q1_title, q1_query)
    print_formatted_query(query.q2_title, q2_query)
    print_formatted_percent_query(query.q3_title, q3_query)
