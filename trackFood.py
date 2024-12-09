from datetime import datetime
from helperFunctions import *

def trackFood(cursor):
    userID = input("Enter a user ID: ")
    while (True):
        if userIDExists(cursor, userID):
            break
        elif userID == "-1":
            return
        else:
            userID=input('UserID does not exist. Please try again or type "-1" to exit: ')

    userInput = input("Enter a date (YYYY-MM-DD): ")
    while True:
        if (userInput == "-1"):
            return
        try:
            date = datetime.strptime(userInput, "%Y-%m-%d")
            break
        except:
            userInput=input('Date is invalid. Please try again or type "-1" to exit: ')
    
    servingName = input("Enter the name of the serving: ")
    while True:
        if servingNameExists(cursor, servingName):
            break
        elif servingName == "-1":
            return
        else:
            servingName=input('Serving name does not exist. Please try again or type "-1" to exit: ')

    log = findLogNumber(cursor, userID)

    insertQuery = """
    INSERT INTO LOG (U_id, Log_num, Log_date, S_name) 
    VALUES 
        (%s, %s, %s, %s);
    """

    cursor.execute(insertQuery, (userID, log, date, servingName))