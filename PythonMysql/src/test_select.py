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

sql = 'select * from person_1'
cursor.execute(sql)

rs = cursor.fetchall()
for row in rs:
    print('userId=%s, userName=%s, age=%s' % row)

# 关闭连接
cursor.close()
conn.close()