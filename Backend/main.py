import pyodbc

sqlDbConn = pyodbc.connect(
"Driver={SQL Server Native Client 11.0};"
"Server=localhost\sqlexpress;"
"Database=StoreAdminDB;"
"Trusted_Connection=yes;"
)


def insertData(sqlDbConn):
    print("Insert")
    cursor = sqlDbConn.cursor()
    cursor.execute(
        "INSERT INTO Items (ItemID,ItemName,ItemDescription,Quantity,ItemPrice) values(?,?,?,?,?)",
        (2,'Bread', 'Pound of Bread', '5', '2.35'))
    sqlDbConn.commit()
    
insertData(sqlDbConn)