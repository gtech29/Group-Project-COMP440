import mysql.connector
import os
from dotenv import load_dotenv
from mysql.connector import errorcode

# load the .env file
load_dotenv()

# retrieve username and password
db_username = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

# use try and except to handle connection errors

try:
  cnx = mysql.connector.connect(  
    user=db_username,
    password=db_password,
    host='localhost',
    database='login_system'
  )
  
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print(cnx)
  cnx.close()