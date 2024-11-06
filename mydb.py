import mysql.connector
dataBase= mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123456789'
)


cursorObject= dataBase.cursor()

cursorObject.execute("CREATE DATABASE dice_db")

print("The database has been created!")