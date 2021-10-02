#creating cursor for database and creatigng a databse
import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='sys',
    password='adarsh123',
   #creating table
    database='iit_ropar'
)

print('connection created')
mycursor=conn.cursor()
print('Cursor created')
#insert into table
mycursor.execute("insert into demo value('adarsh','punjab','15555')")
conn.commit()
print ('values ceated')
#fetch data
mycursor.execute("select * from demo ")
myreslt=mucyrsor.fetchall()
for i in myreslt:
    print('data fetched')
    #fetch multiple vale
    mycursor.execute("select * from demo where name='python' ")
    myreslt = mucyrsor.fetchall()
    for i in myreslt:
        print('data fetched')
        #delete
        mycursor.execute("delete from demo where name='python' ")
     conn.commit()
print('value deleted')

#mycursor.execute("create table demo(name varchar(50),address varchar(50),phonr varchar(50)")
#mycursor.execute("creat database IIT_Ropar")
#print('databse made')