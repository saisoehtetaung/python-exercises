import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="123456",
  database="mydatabase"
)

sql= "insert into customers (name,address) values (%s,%s)"
values= [('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')]
mycursor = mydb.cursor()

mycursor.executemany(sql,values)
mydb.commit()

print(mycursor.rowcount,"record inserted")


mycursor.execute("select * from customers")
for i in mycursor:
    print(i)





