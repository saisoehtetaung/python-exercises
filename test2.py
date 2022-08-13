import sqlite3

cnn=sqlite3.connect('test.sqlite')
cur=cnn.cursor()

cur.execute('DROP TABLE IF EXISTS STUDENT')

cur.execute('CREATE TABLE STUDENT(ID INT(10) PRIMARY KEY ,NAME VARCHAR(100))')
name1=input("Enter Name1:")
cur.execute('INSERT INTO STUDENT (ID,NAME) VALUES (1,?)',(name1,))
name2=input("Enter Name2:")
cur.execute('INSERT INTO STUDENT (ID,NAME) VALUES (2,?)',(name2,))
cnn.commit()
sql=cur.execute('SELECT * FROM STUDENT')
for name in sql:
    print(name[0],name[1])

cur.close()

