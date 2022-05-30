import pypyodbc
import pandas as pd

SERVER_NAME = 'DESKTOP-GF92BLF'
DATABASE_NAME = 'Sarvar_Elite'

conn = pypyodbc.connect("""
    Driver={{SQL Server Native Client 11.0}};
    Server={0};
    Database={1};
    Trusted_connection=yes;""".format(SERVER_NAME, DATABASE_NAME)
)

sql_query = """ 
Select Top 100 * from tblDepartment
"""

df1 = pd.read_sql(sql_query, conn)



import pyodbc # pip install pypyodbc
import pandas as pd # pip install pandas

SERVER_NAME = 'DESKTOP-GF92BLF'
DATABASE_NAME = 'Sarvar_Elite'

conn = pyodbc.connect("""
    Driver={{SQL Server Native Client 11.0}};
    Server={0};
    Database={1};
    Trusted_Connection=yes;""".format(SERVER_NAME, DATABASE_NAME)
)

sql_query = """
spentries
"""
sql_query2 = '''
'''

# With Headers
df1 = pd.read_sql(sql_query, conn)

df1.to_excel (r'C:\Users\Sidak\Desktop\export_dataframe.xlsx', index = False, header=True)

df2 = df1.loc[5,:]

# df2 = pd.read_sql(sql_query2, conn)




import pandas

from openpyxl import load_workbook

book = load_workbook('export_dataframe.xlsx')

writer = pandas.ExcelWriter('export_dataframe.xlsx', engine='openpyxl') 

writer.book = book

writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

data_filtered.to_excel(writer, "Main", cols=['Diff1', 'Diff2'])

writer.save()

df2 = df1.loc[0,:]