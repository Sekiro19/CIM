from PySide6.QtSql import *

DRIVER = "SQL Server Native Client 11.0"
SERVER = "LDZ-JH12YIQYAKP\\SQLEXPRESS"
DATABASE = 'DDA'
def setConnectionString(User: str, password: str):
    db = QSqlDatabase.addDatabase("QODBC")
    CONNSTRING = f"Driver={DRIVER};Server={SERVER};Database={DATABASE};UID={User};PWD={password};"
    db.setDatabaseName(CONNSTRING)
    if db.open():
        return True
    else:
        error = db.lastError()
        error_message = f"Error connecting to database: {error.text()}"
        return error_message
    
result = setConnectionString('SU', '147895623Sekiro')
print(result)

# Driver={SQL Server Native Client 11.0};Server=LDZ-JH12YIQYAKP\SQLEXPRESS;Database=DDA;Trusted_Connection=yes;