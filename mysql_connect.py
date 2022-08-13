import mysql.connector;

# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "admin",
#     password = "123456"
# );

mydb = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "123456",
    database = "mydatabase"
);


# print(mydb);
# cursor = mydb.cursor();

# cursor.execute("select database()");
# data = cursor.fetchone();

# print("Connection established is : ",data);

cursor = mydb.cursor();
# cursor.execute("drop database if exists mydatabase");
# cursor.execute("create database mydatabase");
# cursor.execute("show databases");
# data = cursor.fetchall();

# print("database list: ",data);

# sql = '''
#     create table employee(
#         name char(100) not null,
#         age int,
#         sex char(1),
#         income float
#     );
# '''
# cursor.execute(sql);
# cursor.execute("desc employee");
# data = cursor.fetchall();
# print("describe employee", data);

# sql = '''
#     insert into employee(name,age,sex,income) values (%s,%s,%s,%s) ;
# ''';

# data = [("Zaw Zaw",20,"m",200000),("Kyaw Gyi",22,"m",400000),("Su Su",23,"f",300000)];

# try:
# cursor.executemany(sql,data);
# mydb.commit();

# where clause
# cursor.execute("select * from employee where income>=0;");
# order by 
# cursor.execute("select * from employee where income>=200000 order by income desc;")

# update data 
# sql = '''update employee set age=age+1 where sex="m";'''

# delete data 
sql = '''delete from employee where age=%d;''' % (23);
try: 
    cursor.execute(sql);
    mydb.commit();
except:
    mydb.rollback();

cursor.execute("select * from employee order by age;");
employee = cursor.fetchall();
print("employee",employee);
# except:
#     mydb.rollback();




mydb.close();