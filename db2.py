# import warnings
import urllib
import pyodbc

def connect(companyID=None, branchID=None):
    result="True"
    print("*********************************result-----------")
    try:
        DB = {'servername': 'tcp:server-india.database.windows.net,1433', 'database': 'MyDatabase', 'username': 'bansi@server', 'password': 'Azure@123'}
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

