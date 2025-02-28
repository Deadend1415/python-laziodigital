import oracledb
######################### CREATE CONNECTION
conn = oracledb.connect(
    user = "SYS",
    password = "root",
    dsn = 'localhost:1521/xe',
    mode = oracledb.SYSDBA
)
print('-----------------------------')
print(conn)
print('-----------------------------')
cursor = conn.cursor()
#########################
def Create_tabelle():
    cursor.execute("""
               CREATE TABLE  ANAGRAFE(
                   NOME VARCHAR2(20),
                   COGNOME VARCHAR2(20),
                   ETA INT
               )
               """)
    print("tabella creata")
# end def

def Insert():
    sql = "INSERT INTO ANAGRAFE (nome,cognome,eta) VALUES (:1,:2,:3)"
    value = ("Mario","Trinetti",30)
    cursor.execute(sql,value)
    conn.commit()
    print("Record Inserted")
    print('-----------------------------')
# end def
Insert()
######################### CLOSE CONNECTION
cursor.close()
conn.close()