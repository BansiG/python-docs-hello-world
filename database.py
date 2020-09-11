
import pandas as pd
import warnings
from sqlalchemy import create_engine
import urllib
import pyodbc

warnings.filterwarnings("ignore")

def get_sqldata(server_name='scan-n-go-server.database.windows.net', table_name='Records', columns='*', companyID=None, branchID=None):
    """
    input:
        server_name str
        table_name str
        columns: default select all; str
    output:
        pd.DataFrame
    """
    DB = {'servername': server_name, 'database': 'ScanNGoDB', 'username': 'sqluser', 'password': 'Azure@123'}
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                          + DB['servername']
                          + ';DATABASE=' + DB['database']
                          + ';UID=' + DB['username']
                          + ';PWD=' + DB['password'])
    cursor = conn.cursor()
    try:
        sql = """SELECT * from Records where (CompanyID = ? AND BranchID = ?)"""
        cursor.execute(sql, (companyID,branchID))
        records = cursor.fetchall()
        
        for row in records:
            cid= row[0]
            bid = row[1]
            date = row[2]
            ver = row[3]
            print("company id is", cid)
            print("branch id is", bid)
            print("version is ", ver)
            print("date is ", date)
        
        Result="Version" + str(ver) + " released on Date" +str(date)    

        # sql = "SELECT ModelVersion FROM Records WHERE CompanyID="
        # val = (companyID, branchID, DateTime, version)
        # cursor.execute(sql, val)
        print('succeed get {} table!'.format(table_name))

        return Result
    except:
        print('check input')


def insert_row(server_name='scan-n-go-server.database.windows.net', table_name='Records', companyID=None, branchID=None, DateTime=None, version=None):
    try:
        DB = {'servername': server_name, 'database': 'ScanNGoDB', 'username': 'sqluser', 'password': 'Azure@123'}
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='
                              + DB['servername']
                              + ';DATABASE=' + DB['database']
                              + ';UID=' + DB['username']
                              + ';PWD=' + DB['password'])
        cursor = conn.cursor()
        sql = """INSERT INTO 'Records'
                              ('CompanyID', 'BranchID', 'DateTime', 'ModelVersion') 
                              VALUES (?, ?, ?, ?);"""
        val = (companyID, branchID, DateTime, version)
        cursor.execute(sql, val)
        print("Record added successfully \n")
        conn.commit()
        print("Succeed!")
        return "True"
    except Exception as ex:
        print("Check again!!!")
        return "False"