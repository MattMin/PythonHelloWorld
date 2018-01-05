import pymysql

conn = pymysql.connect(
    host = '192.168.8.39',
    port = 3306,
    user = 'root',
    password = 'root',
    database = 'test',
    charset = 'utf8'
)

cursor = conn.cursor()

print(conn)
print(cursor)

cursor.close()
conn.close()