import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
#mycursor.execute("select * from test1.test_table1")  #For printing all table 
mycursor.execute("select c1,c5 from test1.test_table1") #For particular columns 
for i in mycursor.fetchall():
    print(i)