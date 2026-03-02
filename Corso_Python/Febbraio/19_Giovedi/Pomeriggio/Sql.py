import mysql.connector as msc

mydb = msc.connect(
    host = "localhost",
    user = "root",
    password = "MySQL93!"
)

# print(mydb)

mycursor = mydb.cursor()
query = "show databases"
mycursor.execute(query)
print(mycursor.fetchall())