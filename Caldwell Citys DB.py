#Matthew Caldwell
#Chapter 14-1




Python Script: "create_cities_db.py"

import sqlite3

#create a database
conn = sqlite3.connect("cities.db")
# create a cursor
cursor = conn.cursor()
#cursor.execute("DROP TABLE IF EXISTS contacts;")
#create a table in the database
cursor.execute("CREATE TABLE IF NOT EXISTS Cities (CityID INTEGER,CityName TEXT, Population REAL);")
# Insert data into Cities table
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (101,'Yark',22000))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (102,'Bark',23000))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (103,'Sidney',33000))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (104,'Berly',56500))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (105,'Colobia',34500))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (106,'Delhi',54670))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (107,'Dubai',78600))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (108,'Texas',98200))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (109,'Hydera',76300))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (110,'Mumbai',99500))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (111,'Udipi',76900))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (112,'Golinda',12700))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (113,'Carlin',26000))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (114,'Holin',67300))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (115,'Humany',34590))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (116,'Doby',23700))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (117,'Japan',87400))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (118,'Totla',97400))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (119,'Welly',34500))
cursor.execute("""INSERT INTO Cities (CityID,CityName,Population)VALUES (?,?,?)""", (120,'Belly',72000))
# List of all cities sorted by population in ascending order
print("1.List of all cities sorted by population in ascending order : \n")
cursor = conn.execute("SELECT * FROM Cities ORDER BY Population")
records = cursor.fetchall()
for row in records:
    print(str(row[0])+"\t"+row[1]+"\t"+str(row[2]))
# List of all cities sorted by population in descending order
print()
print("2.List of all cities sorted by population in descending order : \n")
cursor = conn.execute("SELECT * FROM Cities ORDER BY Population DESC")
records = cursor.fetchall()
for row in records:
    print(str(row[0])+"\t"+row[1]+"\t"+str(row[2]))
#  List of all cities sorted by Name  
print()
print("3.List of all cities sorted by Name :\n")
cursor = conn.execute("SELECT * FROM Cities ORDER BY CityName")
records = cursor.fetchall()
for row in records:
    print(str(row[0])+"\t"+row[1]+"\t"+str(row[2]))
# The Total & Average Population of all cities
print()
total_pop=0
cnt=0
cursor = conn.execute("SELECT Population FROM Cities")
records = cursor.fetchall()
for row in records:
    total_pop=total_pop+row[0];
    cnt=cnt+1
print("4.The Total Population of all cities : ",total_pop)
print("5.The Average Population of all cities : ",round(total_pop/cnt,2))
# The City with Highest & Lowest Population
cursor = conn.execute("SELECT CityName FROM Cities WHERE Population = (SELECT MAX(Population) FROM Cities)")
records = cursor.fetchall()
for row in records:
    print("6.The City with Highest Population :",row[0])

cursor = conn.execute("SELECT CityName FROM Cities WHERE Population = (SELECT MIN(Population) FROM Cities)")
records = cursor.fetchall()
for row in records:
    print("7.The City with Lowest Population :",row[0])
