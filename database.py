
# import warnings
import urllib
# import mysql.connector
# from mysql.connector import errorcode
# import pymysql.cursor
import pyodbc

# warnings.filterwarnings("ignore")
"""
def connect(server_name='tcp:server-india.database.windows.net,1433', companyID=None, branchID=None):

    config = {
      'host':'scan-n-go-server.database.windows.net',
      'user':'bansi@server',
      'password':'Azure@123',
      'database':'MyDatabase',
      'cursorclass':pymysql.cursors.DictCursor
    }
    result="True"
    # Construct connection string
    try:
      conn = pymysql.connect(**config)
      
      print("Connection established")
    except Exception as err:
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

"""

def connect(server_name='tcp:server-india.database.windows.net,1433', companyID=None, branchID=None):
    result="True"
    try:
        DB = {'servername': server_name, 'database': 'MyDatabase', 'username': 'bansi', 'password': 'Azure@123'}
        # conn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=scan-n-go-server.database.windows.net,1433', user='sqluser@server', password='Azure@123', database='ScanNGoDB')
        conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};Server='
                              + DB['servername']
                              + ';Database=' + DB['database']
                              + ';Uid=' + DB['username']
                              + ';Pwd=' + DB['password']
                              )
        cursor = conn.cursor()
        result = "connnected"
    except Exception as ex:
        result = str(ex)
    return result
        # print('check input')

