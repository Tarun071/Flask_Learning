import mysql.connector as sq

conn=sq.connect(
host='localhost',
user='root',
password='root',
database='flaskdb'
)
print("connection succesfull")

cursor=conn.cursor()

# try: 
#     cursor.execute(
#     "CREATE TABLE users( id INT PRIMARY KEY AUTO_INCREMENT,username VARCHAR(100),email VARCHAR(100),password VARCHAR(255),created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
#     )
#     conn.commit()
#     print("Table created succesfully")
# except Exception as e :
#     pass
    # print("table already exist",e)

