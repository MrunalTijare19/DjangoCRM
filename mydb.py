# Install MySql on your computer
# http://dev.mysql.com/download/installer
# pip install mysql
# pip install mysql-connector 
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Yuvraj@19'
)

# prepare Cursor Object 
cursorObject = dataBase.cursor()

# Create database 
cursorObject.execute("CREATE DATABASE customer")

print('All Done!!')