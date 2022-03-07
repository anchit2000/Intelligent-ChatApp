import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Anchit@1234",
    database="chat_application"
)

cursor = conn.cursor()

if __name__ == '__main__':
    print(conn)
    cursor.execute("SHOW tables;")
    print(cursor.fetchall())