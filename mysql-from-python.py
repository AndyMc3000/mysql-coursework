import os
import pymysql

# Get username (environment variable) from os
username = os.getenv("C9_USER")

connection = pymysql.connect(host='LocalHost',
                             user=username,
                             password='',
                             db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection regardless of whether the above was successful
    connection.close()
