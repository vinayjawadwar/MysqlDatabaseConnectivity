import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="vinay",passwd="1234")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

for i in mycursor: 
     print(i)
     
