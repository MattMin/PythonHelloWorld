import pymysql

# 创建connection
conn = pymysql.connect(
    host='192.168.8.39',
    port=3306,
    user='root',
    password='root',
    database='test',
    charset='utf8'
)

# 获取connection的cursor
cursor = conn.cursor()

print(conn)
print(cursor)

# 关闭连接
cursor.close()
conn.close()