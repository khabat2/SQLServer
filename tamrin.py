import pyodbc

connection = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                      "Server=.;"
                      "Database=pythonTosegar;"
                      "Trusted_Connection=yes;")

curser = connection.cursor()
curser.execute("CREATE TABLE Employees"
               "( EmployeeID INT PRIMARY KEY IDENTITY(1, 1),"
               "FirstName NVARCHAR(50),"
               "LastName NVARCHAR(50)ProductionLineID INT ,"
               "CONSTRAINT FK_ProductionLine FOREIGN KEY(ProductionLineID)"
               " REFERENCES ProductionLines(ProductionLineID),"
               "); ")
curser.commit()

curser.execute("CREATE TABLE ProductionLines"
               "(ProductionLineID INT PRIMARY KEY IDENTITY(1, 1)"
               ",ProductionLineName NVARCHAR(100));"
               " ")
curser.commit()

curser.execute("INSERT INTO Employees"
               "(FirstName, LastName)"
               "VALUES"
               "('ahmad', 'karimi'),"
               "('reza', 'sediqi'),"
               "('sara', 'ramezani');"
               " ")
curser.commit()

curser.execute("INSERT INTO ProductionLines(ProductionLineName)"
               "VALUES"
               "('Production Line 1'),"
               "('Production Line 2'),"
               "('Production Line 3');"
               " ")
curser.commit()

curser.execute("SELECT FirstName+' '+LastName"
               " AS FullName,"
               " PrdLineName FROM Employee "
               " INNER JOIN ProductionLines "
               " ON Employee.PrdLineID=ProductionLines.PrdLineID ")
curser.commit()

# added
