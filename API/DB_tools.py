import mysql.connector
import env
import time
import json
import csv
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4
from psycopg2 import sql as sqlhelper
import qrcode


def create_id():
    random_name = str(uuid4())
    random_name = random_name.replace("-","")
    random_name = "001_"+random_name
    return random_name


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

def DB_COMMIT_MULTIPLE(statement,values):
    mydb = mysql.connector.connect(
    host=env.MYSQL_HOST,
    port=3306,
    user= env.MYSQL_USER,
    password = env.MYSQL_PASSWORD,
    database=env.MYSQL_DB    
)
    mycursor = mydb.cursor(buffered=True)

    mycursor.executemany(statement,values)
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

# def DB_JSON_NONULL(table_name):
#     mydb = mysql.connector.connect(
#     host=env.MYSQL_HOST,
#     port=3306,
#     user= env.MYSQL_USER,
#     password = env.MYSQL_PASSWORD,
#     database=env.MYSQL_DB  
        
#         )
#     mycursor = mydb.cursor(buffered=True)
#     mycursor.execute(""" 
#                      SELECT
#                 count(*)
#             FROM
#                 {table_name}
#         """).format(
#             table_name = sqlhelper.Identifier(table_name),
#         )
#     print(table_name)
#     row_headers = [x[0] for x in mycursor.description]
#     rv = mycursor.fetchall()
#     data = []
#     for result in rv[::-1]:
#         # data.append(dict(zip(row_headers, result)))
#         print(result)
#         check_none_choose = row_headers.index('choose_id')
#         check_none_text = row_headers.index('text_id')
#         # if result[check_none_text]==None: result = result[0:check_none_choose]+result[check_none_text:]
#         # if result[check_none_text]==None: result = result[0:check_none_text]
#         query_piece = [(row_headers[i],result[i]) for i in range(len(result)) if result[i]!=None ]
#         data.append(dict(zip(row_headers, result)))

        

#     mydb.close()
#     mycursor.close()

#     return data


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


def create_QR_code(quiz_id,qr_text):
    qr = qrcode.QRCode(
        border = 1,
        box_size=20       
    )
    
    
    qr_text = str(qr_text)
    
    qr.add_data(qr_text)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(f'./api_public/QR/{quiz_id}.png')
    event_info = {"ID": quiz_id, "Path": event_path } #решить, нужно ли это
    add_text_to_QR(title, f'{quiz_id}.png', dynamic)
    

    
    
    return 

