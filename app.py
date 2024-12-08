import mysql.connector as connector
from createDatabase import *
from visualizeDB import *

cnx = connector.connect(user='root', host='127.0.0.1', password='5673')
cursor = cnx.cursor()

createDB(cursor)
insertData(cursor)
visualizeData(cursor)