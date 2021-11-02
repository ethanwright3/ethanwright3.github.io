
#Table Creation
import pymysql

conn = pymysql.connect(
        host= 'database-1-instance-1.coig4wr2sngc.us-east-2.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = '88888888',
        db = 'icuneedbeds',
        )

#Table Creation
cursor=conn.cursor()
create_table="""
create table Details (name varchar(200),email varchar(200),comment varchar(200),gender varchar(20) )"""
cursor.execute(create_table)

#insert query
def insert_details(name,email,comment,gender):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
    conn.commit()
#read the data
def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details