import os
import pymysql

# Get username (environment variable) from os
username = os.getenv("C9_USER")

connection = pymysql.connect(host='LocalHost',
                             user=username,
                             password='',
                             db='Chinook')
# The above doesn't change, just add each block of code below to achieve the function
# Example 1
try:
    # Run a query - connectint to MySql from Python
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection regardless of whether the above was successful
    connection.close()


# Example 2 - Cursor
try:
    # Run a cursor query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = "select * from Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
finally:
    # Close the connection regardless of whether the above was successful
    connection.close()

# Example 3 - Create a table
try:
    # Run a cursor query
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
    # The above will display a warning but thats ok

finally:
    # Close the connection regardless of whether the above was successful
    connection.close()

# Example 4- Adding a row/data to a table
try:
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
finally:
    connection.close()

# Example 5- Adding multiple rows/data to a table
try:
    with connection.cursor() as cursor:
        rows = [("bob", 21, "1990-02-06 23:04:56"),
                ("jim", 56, "1955-05-09 13:12:45"),
                ("fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
finally:
    connection.close()

# Example 6 - Update table
try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 22 where name = 'Bob';")
        connection.commit()
finally:
    connection.close()

# Example 7 - Alternate way to Update table

try:
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s where name = %s;",
                       (23, 'Bob'))
        connection.commit()
finally:
    connection.close()

# Example 8 - Update Many
try:
    with connection.cursor() as cursor:
        rows = [(23, 'Bob'),
                (24, 'Jim'),
                (25, 'Fred')]
        cursor.executemany("UPDATE Friends SET age = %s where name = %s;",
                           rows)
        connection.commit()
finally:
    connection.close()

# Example 9 - Delete
try:
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
        connection.commit()
finally:
    connection.close()

# Example 10 - Alternate Delete
try:
    with connection.cursor() as cursor:
        row = cursor.execute("DELETE FROM Friends where name = %s", 'Bob')
        connection.commit()
finally:
    connection.close()

# Example 11 - Delete Many
try:
    with connection.cursor() as cursor:
        row = cursor.executemany(
            "DELETE FROM Friends where name = %s", ['Bob', 'Jim'])
        connection.commit()
finally:
    connection.close()

# Example 12 - Delete Where In
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