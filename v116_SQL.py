import pyodbc

connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=.;"
                      "Database=pythonTosegar;"
                      "Trusted_Connection=yes;")

curser = connection.cursor()
curser.execute("INSERT INTO personal(prsl_name,prsl_family, prsl_age) VALUES ('ahmad', 'babayi', 32)")
curser.commit()
