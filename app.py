import mysql.connector as connector
from createDatabase import *
from visualizeDB import *
from trackFood import trackFood

cnx = connector.connect(user='root', host='127.0.0.1', password='5673')
cursor = cnx.cursor()

createDB(cursor)
insertData(cursor)
trackFood(cursor)
visualizeData(cursor)

cursor.close()
cnx.close()