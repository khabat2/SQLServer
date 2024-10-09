import pyodbc

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=.;"
                      "Database=pythonTosegar;"
                      "Trusted_Connection=yes;")
cursor = conn.cursor()


class Repository():
    def __init__(self):
        pass

    def Create(self, TableName, col, val):
        try:
            cursor.execute("INSERt INTO " + TableName + " (" + col + ") VALUES(" + val + ")")
            cursor.commit()
            return True
        except:
            return False

    def Read(self, TableName, col):
        try:
            return cursor.execute("SELECT " + col + "  FROM " + TableName)

        except:
            return ()

    def Search(self, TableName, col, where):
        try:
            return cursor.execute("SELECT " + col + "  FROM " + TableName + " where " + where)

        except:
            return ()

    def Update(self, TableName, col, where):
        try:
            cursor.execute("update " + TableName + " set " + col + " where " + where + "")
            cursor.commit()
            return True
        except:
            return False

    def Delet(self, TableName, where):
        try:
            cursor.execute("delete from " + TableName + " where " + where)
            cursor.commit()
            return True
        except:
            return False
