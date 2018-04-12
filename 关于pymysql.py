import pymysql

user = input("用户名：").strip()
pwd = input("密码：").strip()

#链接
conn = pymysql.connect(host="localhsot",user="root",password="",database="test1",charset="utf8")

#游标
cursor = conn.cursor() #执行完毕返回的结果默认以元祖显示

#执行sql语句
sql = 'select * from userinfo where name="%s" and password="%s"' %(user,pwd)#注意%s需要加引号
print(sql)
res = cursor.execute(sql) #执行sql语句，返回sql查询的结果
print(res)

cursor.close()
conn.close()

if res:
    print("登陆成功")
else:
    print("登录失败")