import mysql.connector

# TODO : These creds should be ENV vars
conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Anchit@1234",
    database="chat_application"
)

cursor = conn.cursor()

if __name__ == '__main__':
    print(conn)
    # cursor.execute("SHOW tables;")
    # print(cursor.fetchall())
    cursor.execute("select * from user_table;")
    a = cursor.fetchall()
    print(a)
    a = [i[1] for i in a]
    print(a)
