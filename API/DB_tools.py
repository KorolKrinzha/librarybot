import mysql.connector
import env
import time
import json
import csv
from werkzeug.security import generate_password_hash, check_password_hash


    

def DB_COMMIT(statement,values):
    mydb = mysql.connector.connect(
    host=env.MYSQL_HOST,
    port=3306,
    user= env.MYSQL_USER,
    password = env.MYSQL_PASSWORD,
    database=env.MYSQL_DB    
)
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute(statement,values)
    mydb.commit()
    
    mydb.close()
    mycursor.close()

    
    return

def DB_JSON(statement,values):
    mydb = mysql.connector.connect(
    host=env.MYSQL_HOST,
    port=3306,
    user= env.MYSQL_USER,
    password = env.MYSQL_PASSWORD,
    database=env.MYSQL_DB  
        
        )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(statement,values)
    row_headers = [x[0] for x in mycursor.description]
    rv = mycursor.fetchall()
    data = []
    for result in rv[::-1]:
        data.append(dict(zip(row_headers, result)))

    mydb.close()
    mycursor.close()

    return data


def DB_FETCH_ONE(statement,values):
    mydb = mysql.connector.connect(
    host=env.MYSQL_HOST,
    port=3306,
    user= env.MYSQL_USER,
    password = env.MYSQL_PASSWORD,
    database=env.MYSQL_DB  
        
        )
    mycursor = mydb.cursor(buffered=True)
    account = mycursor.execute(statement,values)
    try:
        account = list(mycursor.fetchone())
    except:
        account = []
    
    mycursor.close()
    mydb.close()
    
    return account

def DB_CHECK_EXISTENCE(statement,values):
    mydb = mysql.connector.connect(
    host=env.MYSQL_HOST,
    port=3306,
    user= env.MYSQL_USER,
    password = env.MYSQL_PASSWORD,
    database=env.MYSQL_DB  
        
        )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute(statement,values)
    row_headers = [x[0] for x in mycursor.description]
    rv = mycursor.fetchall()
    data = []
    for result in rv[::-1]:
        data.append(dict(zip(row_headers, result)))
   
    existence_value = data[0]['COUNT(1)']
    return bool(existence_value)


