import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

mycursor.execute("CREATE DATABASE if not exists test1")
mycursor.execute("CREATE TABLE if not exists test1.test_table1 (NAME VARCHAR(50), MOBILE VARCHAR(10), AGE INT , WEIGHT FLOAT)")
mycursor.execute("insert into test1.test_table1 values('VAIBHAV','123456789',20,66.5)")
mydb.commit()
mycursor.execute("select * from test1.test_table1")
for i in mycursor.fetchall():
  print(i)
mydb.close()



"""
CORRSEPONDING SQL COMMANDS
CREATE DATABASE if not exists test;
CREATE TABLE test.test_table(NAME VARCHAR(50), MOBILE VARCHAR(10), AGE INT , WEIGHT FLOAT);
SHOW DATABASES;
INSERT INTO test.test_table(NAME,MOBILE,AGE,WEIGHT)
VALUES ("VAIBHAV","1234567890",19,70.2);

select * from test.test_table;

"""