import pymysql

# 创建connection
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='root',
    database='test',
    charset='utf8'
)

# 获取connection的cursor
cursor = conn.cursor()

sql = 'select * from person_1'
cursor.execute(sql)

print(cursor.rowcount)

rs = cursor.fetchone()
print(rs)

rs = cursor.fetchmany(2)
print(rs)

rs = cursor.fetchall()
print(rs)

cursor.close()
conn.close()