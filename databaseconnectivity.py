import pymysql
connection=pymysql.connect(host='127.0.0.1',user='root',password='',db='phdbtech')
print("Connection established")
mycusrsor=connection.cursor()
'''
query1="create table test(name varchar(25),age int (3))"
mycusrsor.execute(query1)
print("table created successfully")

#insert="insert into test(name,age) values('ram',33)"
name=input("enetr your name")
age=int(input("enetr your age"))
insert="insert into test(name,age) values(%s,%s)"
value=(name,age)
mycusrsor.execute(insert,value)
'''
upd="update test set name='ashwani' where age=100"
mycusrsor.execute(upd)
connection.commit() # when we insert,update,delete to save data permananenly
print("Data inserted successfully")
connection.close()