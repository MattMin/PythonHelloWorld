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

sql_insert = 'insert into person_1(name, age) VALUE ("周芷若", 20)'
sql_update = 'update person_1 set name = "曹操的儿子" WHERE id = 1'
sql_delete = 'delete from person_1 WHERE id = 2'

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)

    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

# 关闭连接
cursor.close()
conn.close()