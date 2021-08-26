import mysql.connector 

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "starter"
)

mycursor = mydb.cursor()

########1. Create database 
mycursor.execute('CREATE DATABASE starter')

########2. Show all Databases
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)


#########3. Creating table 
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255) )")

#########4. Check if table is exist or not
mycursor.execute('SHOW TABLES')
for x in mycursor:
    print(x)

########5. Primary key 
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

########6. Insert data into table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("gaurav", "dehradun")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted")

## get the id of last row

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("you", "another planet")
mycursor.execute(sql, val)

mydb.commit()

print('id of last row', mycursor.lastrowid)

########## 7. Use of SELECT
mycursor.execute('SELECT * FROM customers')
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


########### 8. User of WHERE
sql = "SELECT * FROM customers  WHERE id = 2"
mycursor.execute(sql)

myresults = mycursor.fetchall()

for x in myresults:
    print(x)


########### 9. Whildcard Characters
sql = "SELECT * FROM customers WHERE address LIKE '%planet%'"

mycursor.execute(sql)

for x in mycursor:
    print(x)

########### 10. Prevent SQL Injection
sql = "SELECT * FROM customers WHERE address = %s"
val = ("planet earth")

mycursor.execute(sql, val)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
    
########### 11. ORDER BY in sql
sql = "SELECT * FROM customers ORDER BY address"
sql = "SELECT * FROM customers ORDER BY id DESC"
mycursor.execute(sql)
for x in mycursor:
    print(x)

########### 12. DELETE FROM BY in sql
sql = "DELETE FROM customers WHERE id = %s"
val = (5,)
mycursor.execute(sql, val)
mydb.commit()

for x in mycursor:
    print(x)


########### 13. Drop a table
sql = "DROP TABLE customers"
mycursor.execute(sql)

# DROP only if Exist
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)

########### 14. UPDATE Table in sql
sql = "UPDATE customers SET address = 'home-town' WHERE address = 'dehradun'"
mycursor.execute(sql)
mydb.commit()

########### 15. LIMIT sql data
sql = "SELECT * FROM customers LIMIT 5"
mycursor.execute(sql)

for x in mycursor:
    print(x)


########### 16. Start from another position
sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
mycursor.execute(sql)

for x in mycursor:
    print(x)

########### 17. SQL JOIN (imp)
