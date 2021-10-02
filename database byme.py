import mysql.connector
conn=mysql.connector.connect(
host='localhost',
user='root',
password='Adarsh123',
    database='iit_ropar',
)

print('connection created')
mycursor= conn.cursor()
print('cursor created')

#mycursor.execute("insert into demo values('adarsh','ropar','12345')")
#conn.commit()
mycursor=conn.cursor()
#mycursor.execute("select * from demo where name='adarsh'")
#myresult=mycursor.fetchall()
#for i in myresult:
    #print(i)
mycursor.execute("delete from demo where name='adarsh'")
conn.commit()
