
import pandas as pd
import warnings
from sqlalchemy import create_engine
import urllib
import mysql.connector
from mysql.connector import errorcode


warnings.filterwarnings("ignore")
def connect(server_name='tcp:scan-n-go-server.database.windows.net,1433', companyID=None, branchID=None):
    """
    input:
        server_name str
        table_name str
        columns: default select all; str
    output:
        version
    """
    config = {
      'host':'scan-n-go-server.database.windows.net',
      'user':'sqluser@server',
      'password':'Azure@123',
      'database':'ScanNGoDB'
    }
    result="True"
    # Construct connection string
    try:
      conn = mysql.connector.connect(**config)
      
      print("Connection established")
    except mysql.connector.Error as err:
      result="Failed"
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with the user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cursor = conn.cursor()
    # try:
    #     DB = {'servername': server_name, 'database': 'ScanNGoDB', 'username': 'sqluser', 'password': 'Azure@123'}
    #     conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=scan-n-go-server.database.windows.net,1433', user='sqluser@server', password='Azure@123', database='ScanNGoDB')
    #     # conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server='
    #     #                       + DB['servername']
    #     #                       + ';Database=' + DB['database']
    #     #                       + ';Uid=' + DB['username']
    #     #                       + ';Pwd=' + DB['password']
    #     #                       )
    #     cursor = conn.cursor()
    #     result = "connnected"
    # except Exception as ex:
    #     result = str(ex)
    return result
        # print('check input')

