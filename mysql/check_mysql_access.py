import mysql.connector

connection = mysql.connector.connect(
    user='holberton_user',
    password='projectcorrection280hbtn',
    host='localhost',
    database='mysql'
)

cursor = cnx.cursor()

try:
    cursor.execute("SHOW GRANTS")
    print("Grants for user holberton_user:")
    for grant in cursor:
        print(grant)
except mysql.connector.Error as e:
    print("Error code:", e.errno)
    print("SQLSTATE:", e.sqlstate)
    print("Error message:", e.msg)

connection.close()
