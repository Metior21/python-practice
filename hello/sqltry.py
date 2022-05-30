
import pyodbc       

def read(conn):
        print("read")
        cursor = conn.cursor()
        cursor.execute('Select * from tblDepartment')
        for row in cursor:
            print(f'row = {row}')
        print()
            
def create(conn):
    print("create")
    coursor = conn.cursor()
    coursor.execute(
        'Insert into tbldepartment(id,Location) values(?,?);',
        (9,'rabba')

    )
    conn.commit()
    read(conn)

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-GF92BLF;"
    "Database=Sarvar_Elite;"
    "Trusted_connection=yes;"
)

read(conn)
create(conn)
conn.close()



import sqlite3
import pyodbc
import pandas as pd

dbconn = sqlite3.connect('Sarvar_Elite') 
c = dbconn.cursor()
                 
c.execute('Select * from tblDepartment')

df = pd.DataFrame(c.fetchall(), columns = ['id', 'Departmetname', 'Location'])
print (df)

