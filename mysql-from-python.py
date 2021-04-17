import os
import datetime
import pymysql

# Get username (environment variable) from os
username = os.getenv("C9_USER")

connection = pymysql.connect(host='LocalHost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)

        connection.commit()
finally:
    connection.close()
