import mysql.connector as connector
from createDatabase import createDB, insertData
from visualizeDB import visualizeData, visualizeStructure
from trackFood import trackFood
from caloriesOnDate import caloriesOnDate
from foodsOnDate import foodsOnDate

#connect to the database server
cnx = connector.connect(user='root', host='127.0.0.1', password='5673')
cursor = cnx.cursor()

createDB(cursor)
insertData(cursor)

print("\nWelcome to the Macro Tracker!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
while True:
    print("What would you like to do?")
    print("1. Log a serving")
    print("2. Show foods logged on date")
    print("3. Calculate calories tracked on date")
    print("4. Visualize data")
    print("5. Visualize structure")
    print("6. Exit")
    print("")
    userInput = input("Enter the number of your choice: ")
    if (userInput == ("1" or "1.")):
        trackFood(cursor)
    elif (userInput == ("2" or "2.")):
        foodsOnDate(cursor)
    elif (userInput == ("3" or "3.")):
        caloriesOnDate(cursor)
    elif (userInput == ("4" or "4.")):
        visualizeData(cursor)
    elif (userInput == ("5" or "5.")):
        visualizeStructure(cursor)
    elif (userInput == ("6" or "6.")):
        break
    else:
        print("Sorry, that input is invalid")
    print("")

cursor.close()
cnx.close()